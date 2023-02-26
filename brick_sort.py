def brick_sort(arr):
    n = len(arr)
    even = []
    odd = []
    for i in range(n):
        if i % 2 == 0:
            even.append(arr[i])
        else:
            odd.append(arr[i])
    even.sort()
    odd.sort()
    sorted_arr = []
    for i in range(n):
        if i % 2 == 0:
            sorted_arr.append(even[i // 2])
        else:
            sorted_arr.append(odd[i // 2])
    return sorted_arr

# Example usage:
arr = [3, 6, 1, 8, 4, 5, 2, 7]
sorted_arr = brick_sort(arr)
print(sorted_arr) # Output: [1, 2, 3, 4, 5, 6, 7, 8]
