def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the index of the target element.
    If the target is not found, return -1.

    Args:
        arr (list of int): Sorted list of integers.
        target (int): The element to search for.

    Returns:
        int: Index of target in arr if found, else -1.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    # Example usage
    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]
    target_value = 7
    index = binary_search(sorted_array, target_value)
    if index != -1:
        print(f"Element {target_value} found at index {index}.")
    else:
        print(f"Element {target_value} not found in the array.")