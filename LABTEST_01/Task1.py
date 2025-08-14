def sum_odd_even(numbers):
    sum_odd = 0
    sum_even = 0
    for num in numbers:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
    return sum_odd, sum_even

if __name__ == "__main__":
    lst = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
    odd_sum, even_sum = sum_odd_even(lst)
    print("Sum of odd numbers:", odd_sum)
    print("Sum of even numbers:", even_sum)
