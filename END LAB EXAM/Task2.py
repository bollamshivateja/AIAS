def merge_sort(arr):
    """
    Sorts an array of parcel weights using Merge Sort algorithm.
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left, right):
    """
    Merges two sorted arrays into a single sorted array.
    This function takes two sorted lists and combines them into a single sorted list
    by comparing elements from both arrays and appending them in ascending order.
    Args:
        left (list): A sorted list of comparable elements.
        right (list): A sorted list of comparable elements.
    Returns:
        list: A single sorted list containing all elements from both left and right arrays
              in ascending order.
    Example:
        >>> merge([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
    Time Complexity: O(n + m), where n is the length of left and m is the length of right.
    Space Complexity: O(n + m) for the result list.
    """
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


if __name__ == "__main__":
    # Get parcel weights from user
    n = int(input("Enter the number of parcels: "))
    
    parcel_weights = []
    print("Enter the weight of each parcel (in kg):")
    for i in range(n):
        weight = float(input(f"Parcel {i+1} weight: "))
        parcel_weights.append(weight)
    
    print("\nOriginal weights:", parcel_weights)
    sorted_weights = merge_sort(parcel_weights)
    print("Sorted weights:", sorted_weights)