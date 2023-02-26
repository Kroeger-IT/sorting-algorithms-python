def gnome_sort(arr):
    n = len(arr)
    i = 0
    while i < n:
        if i == 0 or arr[i] >= arr[i-1]:
            i += 1
        else:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
gnome_sort(arr)
print(arr)
