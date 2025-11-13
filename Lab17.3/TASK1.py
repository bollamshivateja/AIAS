import pandas as pd
import re
import os

# ===============================
# 1. Load CSV file
# ===============================

# Try both the local file and the absolute path
local_path = "social_media.csv"
abs_path = r"C:\Users\Sanjana\OneDrive\Desktop\AIAC\Lab17.3\social_media.csv"

if os.path.exists(local_path):
    path = local_path
elif os.path.exists(abs_path):
    path = abs_path
else:
    raise FileNotFoundError(
        f"CSV file not found. Please put 'social_media.csv' in the same folder as this script, "
        f"or ensure it exists at '{abs_path}'.\n"
        f"Current working directory: {os.getcwd()}"
    )

# Read the CSV safely
df = pd.read_csv(path, encoding="utf-8", encoding_errors="ignore")

print(f"Loaded CSV from: {path}")
print("Initial dataset shape:", df.shape)

# ===============================
# 2. Handle missing values in likes and shares
# ===============================

print("Missing before:", df[['likes', 'shares']].isna().sum().to_dict())

df['likes'] = pd.to_numeric(df['likes'], errors='coerce')
df['shares'] = pd.to_numeric(df['shares'], errors='coerce')

likes_median = df['likes'].median(skipna=True)
shares_median = df['shares'].median(skipna=True)

df['likes'] = df['likes'].fillna(likes_median).clip(lower=0)
df['shares'] = df['shares'].fillna(shares_median).clip(lower=0)

# Use .astype(int) only if there are no NaNs left
df['likes'] = df['likes'].astype(int)
df['shares'] = df['shares'].astype(int)

print("Missing after:", df[['likes', 'shares']].isna().sum().to_dict())

# ===============================
# 3. Clean text: remove stopwords, punctuation, symbols
# ===============================

STOPWORDS = {
    'the', 'is', 'at', 'which', 'on', 'and', 'a', 'an', 'to', 'in', 'for', 'of', 'with', 'by', 'from',
    'it', 'this', 'that', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had', 'do', 'does', 'did',
    'will', 'would', 'could', 'should', 'may', 'might', 'must', 'can', 'shall', 'i', 'you', 'he', 'she',
    'we', 'they', 'me', 'him', 'her', 'us', 'them', 'my', 'your', 'his', 'our', 'their'
}

def clean_text(text):
    if pd.isna(text):
        return ""
    text = str(text).lower()
    text = re.sub(r'<[^>]+>', '', text)                 # remove HTML tags
    text = re.sub(r'http[s]?://\S+', '', text)          # remove URLs
    text = re.sub(r'[^a-z0-9\s]', ' ', text)            # remove punctuation/symbols
    text = re.sub(r'\s+', ' ', text).strip()            # normalize spaces
    words = [w for w in text.split() if w not in STOPWORDS and len(w) > 1]
    return ' '.join(words)

df['post_text_clean'] = df['post_text'].apply(clean_text)

# ===============================
# 4. Convert timestamp to datetime and extract features
# ===============================

df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
df['hour'] = df['timestamp'].dt.hour
df['weekday'] = df['timestamp'].dt.day_name()

# ===============================
# 5. Detect and remove spam
# ===============================

def is_spam(text):
    if pd.isna(text) or len(str(text)) < 5:
        return True
    text_l = str(text).lower()
    words = text_l.split()
    if len(words) > 0 and (len(set(words)) / len(words)) < 0.3:
        return True
    if len(text_l) > 500:
        return True
    if re.search(r'[^a-z0-9\s]{10,}', text_l):
        return True
    return False
df['is_spam'] = df['post_text_clean'].apply(is_spam)
spam_count = int(df['is_spam'].sum())
df = df[~df['is_spam']].drop(columns=['is_spam']).reset_index(drop=True)
# ===============================
# 6. Remove duplicate posts
# ===============================
duplicate_mask = df.duplicated(subset=['post_text_clean'], keep='first')
duplicate_count = int(duplicate_mask.sum())

df = df[~duplicate_mask].reset_index(drop=True)

# ===============================
# 7. Preview results
# ===============================

print({
    'spam_removed': spam_count,
    'duplicates_removed': duplicate_count,
    'rows_remaining': len(df)
})

print("\nSample cleaned data:")
print(df[['post_text', 'post_text_clean', 'timestamp', 'hour', 'weekday']].head().to_string())

# ===============================
# 8. Save cleaned dataset
# ===============================

output_file = "social_media_cleaned.csv"
df.to_csv(output_file, index=False)

print({
    'csv_created': output_file,
    'rows': len(df),
    'cols': len(df.columns)
})
