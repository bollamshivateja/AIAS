import pandas as pd
import numpy as np
import re
import os
from collections import Counter

def clean_review_text(text):
    """Lowercase and remove HTML tags from review text."""
    if pd.isnull(text):
        return ""
    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    # Lowercase
    return text.lower()

def preprocess_movie_reviews(input_csv='movie_reviews-1.csv', output_csv=None):
    # Load data (robust path + encoding)
    candidate_paths = [
        input_csv,
        r"C:\\Users\\pooda\\OneDrive\\Desktop\\AIAC\\LAB 17.3\\movie_reviews-1.csv",
    ]
    path = next((p for p in candidate_paths if os.path.exists(p)), None)
    if path is None:
        raise FileNotFoundError(f"Could not find CSV. Checked: {candidate_paths}")
    df = pd.read_csv(path, encoding='utf-8', encoding_errors='ignore')
    before_summary = {
        "num_rows": len(df),
        "num_missing_ratings": df['rating'].isnull().sum(),
        "rating_min": df['rating'].min(),
        "rating_max": df['rating'].max(),
        "sample_reviews": df['review_text'].head(3).tolist()
    }

    # Clean review text
    df['review_text_clean'] = df['review_text'].apply(clean_review_text)

    # Ensure rating is numeric and handle missing ratings: fill with median
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
    median_rating = df['rating'].median()
    df['rating_filled'] = df['rating'].fillna(median_rating)

    # Normalize ratings to 0-1
    df['rating_normalized'] = df['rating_filled'] / 10.0

    # TF-IDF encoding (no external deps)
    docs = df['review_text_clean'].fillna("").astype(str).tolist()
    tokenized = [t.split() for t in docs]
    N = len(tokenized)
    # document frequency
    dfreq = Counter()
    for toks in tokenized:
        dfreq.update(set(toks))
    # idf with smoothing
    idf = {term: np.log((1 + N) / (1 + dfreq[term])) + 1.0 for term in dfreq}
    # build vocabulary (limit size if needed)
    vocab = sorted(idf.keys())
    tfidf_rows = []
    for toks in tokenized:
        counts = Counter(toks)
        total = float(len(toks)) if len(toks) else 1.0
        row = {f"tfidf_{term}": (counts[term] / total) * idf[term] for term in vocab}
        tfidf_rows.append(row)
    tfidf_df = pd.DataFrame(tfidf_rows).fillna(0.0)

    # Concatenate TF-IDF features with main DataFrame
    df_final = pd.concat([df.reset_index(drop=True), tfidf_df.reset_index(drop=True)], axis=1)

    after_summary = {
        "num_rows": len(df_final),
        "num_missing_ratings": df_final['rating_filled'].isnull().sum(),
        "rating_min": df_final['rating_normalized'].min(),
        "rating_max": df_final['rating_normalized'].max(),
        "sample_clean_reviews": df_final['review_text_clean'].head(3).tolist(),
        "tfidf_feature_count": tfidf_df.shape[1]
    }

    print("=== BEFORE CLEANING ===")
    for k, v in before_summary.items():
        print(f"{k}: {v}")
    print("\n=== AFTER CLEANING ===")
    for k, v in after_summary.items():
        print(f"{k}: {v}")

    # Save cleaned dataset if requested
    if output_csv:
        df_final.to_csv(output_csv, index=False)
    return df_final

# Example usage and test cases
if __name__ == "__main__":
    cleaned_df = preprocess_movie_reviews('movie_reviews-1.csv', 'movie_reviews_cleaned.csv')

    # --- Test Cases ---
    # 1. Check that all review_text_clean are lowercase and have no HTML tags
    assert all('<' not in txt and txt == txt.lower() for txt in cleaned_df['review_text_clean']), "Text cleaning failed"

    # 2. Check that there are no missing values in rating_filled
    assert cleaned_df['rating_filled'].isnull().sum() == 0, "Missing ratings not filled"

    # 3. Check that all normalized ratings are between 0 and 1
    assert cleaned_df['rating_normalized'].between(0, 1).all(), "Ratings not normalized to 0-1"

    print("\nAll test cases passed.")