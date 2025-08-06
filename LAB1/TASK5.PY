def count_word_frequency():
    user_input = input("Enter a string: ")
    words = user_input.split()
    frequency = {}
    for word in words:
        word = word.lower()
        frequency[word] = frequency.get(word, 0) + 1
    for word, count in frequency.items():
        print(f"{word}: {count}")

count_word_frequency()