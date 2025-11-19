from typing import List, Tuple


def divide_and_conquer_min_max(arr: List[int]) -> Tuple[int, int]:
    """
    Returns (min, max) of arr using divide and conquer.
    Raises ValueError for empty list.
    """
    if not arr:
        raise ValueError("arr must not be empty")

    def helper(l: int, r: int) -> Tuple[int, int]:
        # If one element
        if l == r:
            return arr[l], arr[l]
        # If two elements
        if r == l + 1:
            if arr[l] <= arr[r]:
                return arr[l], arr[r]
            else:
                return arr[r], arr[l]
        # More than two elements: split
        mid = (l + r) // 2
        min1, max1 = helper(l, mid)
        min2, max2 = helper(mid + 1, r)
        return (min(min1, min2), max(max1, max2))

    return helper(0, len(arr) - 1)


if __name__ == "__main__":
    # Allow optional command-line args or user input; fall back to default list
    import sys

    default_list = [12, -3, 45, 0, 99, 23, -50, 7, 88, 5, 14, 42]

    if len(sys.argv) > 1:
        try:
            test_list = [int(x) for x in sys.argv[1:]]
        except ValueError:
            print("Command-line arguments must be integers. Using default list.")
            test_list = default_list
    else:
        s = input("Enter integers separated by spaces (press Enter to use default): ").strip()
        if s:
            try:
                test_list = [int(x) for x in s.split()]
            except ValueError:
                print("Invalid input; using default list.")
                test_list = default_list
        else:
            test_list = default_list

    mn, mx = divide_and_conquer_min_max(test_list)
    # Echo the input used and the results
    print("Input:", test_list)
    print("Minimum:", mn)
    print("Maximum:", mx)