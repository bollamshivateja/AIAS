
if __name__ == "__main__":
    lst = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
    unique_sorted = sorted(set(lst))
    print("Sorted list without duplicates:", unique_sorted)
