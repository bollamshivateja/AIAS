def sum(num):
    print(f"Sum of 1 to {num} is :")
    sum = 0
    for i in range(1, num + 1):  # changed num to num+1 to include the last number
        sum = sum + i
    return sum 

num = int(input("Enter the number:"))
print(f"Sum of first n is : {sum(num)}")