def find_common(a, b):
    return [i for i in a for j in b if i == j]
print(find_common([1, 2, 3, 4, 5],[1, 2, 3, 4, 5]))
print(find_common(['apple', 'banana', 'cherry'],['banana', 'kiwi', 'apple']))
