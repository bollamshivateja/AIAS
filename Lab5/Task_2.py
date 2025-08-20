
import re

# Example sentiment lexicon (for demonstration)
positive_words = {"good", "happy", "excellent", "great", "fantastic", "love", "wonderful", "amazing"}
negative_words = {"bad", "sad", "terrible", "awful", "hate", "horrible", "worst", "poor"}

# Example of biased words (for demonstration)
biased_words = {"always", "never", "everyone", "nobody"}

def clean_text(text):
    # Lowercase and remove non-alphabetic characters
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

def detect_bias(text):
    found_bias = [word for word in biased_words if word in text.split()]
    return found_bias

def sentiment_analysis(text):
    text = clean_text(text)
    words = set(text.split())
    pos_count = len(words & positive_words)
    neg_count = len(words & negative_words)
    bias_found = detect_bias(text)
    
    if bias_found:
        print(f"Warning: Potential bias detected in input: {', '.join(bias_found)}")
    
    if pos_count > neg_count:
        return "Positive"
    elif neg_count > pos_count:
        return "Negative"
    else:
        return "Neutral"

def main():
    user_input = input("Enter a sentence for sentiment analysis: ")
    sentiment = sentiment_analysis(user_input)
    print(f"Sentiment: {sentiment}")

if __name__ == "__main__":
    main()
