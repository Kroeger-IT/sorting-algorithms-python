def pancake_sort(arr):
    """
    Sorts the input array using the pancake sort algorithm.
    """
    n = len(arr)
    for i in range(n, 1, -1):
        # Find the index of the maximum element in the first i elements
        max_index = arr.index(max(arr[:i]))

        if max_index != i-1:
            # If the maximum element is not already at the end of the array,
            # flip the elements from the beginning of the array to the maximum element
            arr[:max_index+1] = reversed(arr[:max_index+1])
            # Then flip the elements from the beginning of the array to the i-th element
            arr[:i] = reversed(arr[:i])

    return arr

  
# Example Usage
  
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_arr = pancake_sort(arr)
print(sorted_arr)
