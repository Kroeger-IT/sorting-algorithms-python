def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
selection_sort(arr)
print(arr)
