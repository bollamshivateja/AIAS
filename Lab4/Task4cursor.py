def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

input_str = input("Enter a string: ")
num_vowels = count_vowels(input_str)
if num_vowels == 1:
    print(f"{input_str} it has 1 vowel.")
else:
    print(f"{input_str} it has {num_vowels} vowels.")
