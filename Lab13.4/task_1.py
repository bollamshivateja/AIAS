numbers = [1, 2, 3, 4, 5]
squares = []
for n in numbers:
    squares.append(n ** 2)
print(squares)
# More Pythonic approach using list comprehension
squares = [n ** 2 for n in numbers]
print(squares)



