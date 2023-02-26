def tim_sort(arr):
    # set the minimum run size for insertion sort
    min_run = 32
    
    n = len(arr)
    
    # perform insertion sort on subarrays of size min_run
    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), n - 1))
    
    # merge the sorted subarrays
    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))
            merge(arr, start, midpoint, end)
        size *= 2
    
    return arr

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1
        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item

def merge(arr, start, mid, end):
    left = arr[start:mid+1]
    right = arr[mid+1:end+1]
    
    k = start
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1
    
    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1

# example usage
my_list = [4, 3, 7, 1, 9, 5, 8, 2, 6]
sorted_list = tim_sort(my_list)
print(sorted_list)
