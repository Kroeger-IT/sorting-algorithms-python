def counting_sort(arr):
    # Determine the range of possible values in the input array
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1
    
    # Initialize count array and output array
    count_arr = [0] * range_val
    output_arr = [0] * len(arr)
    
    # Count the occurrences of each element in the input array
    for i in range(len(arr)):
        count_arr[arr[i] - min_val] += 1
    
    # Calculate the cumulative count of each element
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]
    
    # Place the elements in the output array in the correct order
    for i in range(len(arr)):
        output_arr[count_arr[arr[i] - min_val] - 1] = arr[i]
        count_arr[arr[i] - min_val] -= 1
    
    return output_arr

# Example usage
arr = [4, 2, 10, 8, 3, 7, 1, 6, 5, 9]
sorted_arr = counting_sort(arr)
print(sorted_arr)
