import string

def remove_punctuation_lowercase(text):
    # Remove punctuation and convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator).lower()

def remove_stopwords(text, stopwords):
    words = text.split()
    filtered_words = [word for word in words if word not in stopwords]
    return ' '.join(filtered_words)

if __name__ == "__main__":
    stop_words = {
        'a', 'an', 'the', 'and', 'or', 'but', 'if', 'while', 'with', 'to', 'of', 'at', 'by', 'for', 'from', 'in', 'on', 'off', 'out', 'over', 'under', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'so', 'such', 'as', 'that', 'this', 'these', 'those', 'it', 'its', 'he', 'she', 'they', 'them', 'his', 'her', 'their', 'you', 'your', 'yours', 'me', 'my', 'mine', 'we', 'us', 'our', 'ours'
    }
    text = input("Enter text: ")
    cleaned_text = remove_punctuation_lowercase(text)
    result = remove_stopwords(cleaned_text, stop_words)
    print("Processed text:", result)
