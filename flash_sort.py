def flash_sort(arr):
    # Find the maximum value in the array
    max_val = max(arr)
    
    # Initialize the distribution list and output list
    dist_list = [0] * len(arr)
    out_list = [0] * len(arr)
    
    # Calculate the number of elements in each bucket
    for i in range(len(arr)):
        dist_list[int(arr[i] / max_val * (len(arr) - 1))] += 1
    
    # Calculate the starting index for each bucket
    for i in range(1, len(dist_list)):
        dist_list[i] += dist_list[i-1]
        
    # Move the elements to their corresponding bucket
    for i in range(len(arr)-1, -1, -1):
        bucket_index = int(arr[i] / max_val * (len(arr) - 1))
        out_list[dist_list[bucket_index]-1] = arr[i]
        dist_list[bucket_index] -= 1
        
    return out_list

# Example usage
arr = [3, 5, 1, 9, 8, 4, 7, 2, 6]
sorted_arr = flash_sort(arr)
print(sorted_arr)
