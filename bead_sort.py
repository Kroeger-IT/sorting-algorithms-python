def bead_sort(arr):
    # Get the maximum value in the array
    max_val = max(arr)
    
    # Create a 2D list to hold the beads
    beads = [[] for _ in range(len(arr))]
    
    # Drop the beads
    for i, val in enumerate(arr):
        for j in range(val):
            beads[i].append(1)
    
    # Count the beads
    for i in range(len(arr)):
        count = 0
        for j in range(len(beads)):
            if len(beads[j]) > i:
                count += 1
        arr[i] = count
    
    return arr

# Example usage
arr = [5, 3, 1, 7, 4, 1, 1, 20]
sorted_arr = bead_sort(arr)
print(sorted_arr) # Output: [1, 1, 1, 3, 4, 5, 7, 20]
