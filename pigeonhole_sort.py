def pigeonhole_sort(arr):
    # find minimum and maximum values in the array
    min_val = min(arr)
    max_val = max(arr)
    
    # determine the range of values
    num_range = max_val - min_val + 1
    
    # create an array of pigeonholes
    holes = [0] * num_range
    
    # populate the pigeonholes with values from the input array
    for val in arr:
        index = val - min_val
        holes[index] += 1
    
    # construct the sorted array from the pigeonholes
    sorted_arr = []
    for i in range(num_range):
        if holes[i] > 0:
            sorted_arr += [i + min_val] * holes[i]
    
    return sorted_arr


# Example Usage

arr = [8, 3, 2, 7, 4, 6, 8]
sorted_arr = pigeonhole_sort(arr)
print(sorted_arr)  # Output: [2, 3, 4, 6, 7, 8, 8]
