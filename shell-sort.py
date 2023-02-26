def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr


# Example usage
arr = [4, 2, 7, 1, 8, 3]
sorted_arr = shell_sort(arr)
print(sorted_arr)  # Output: [1, 2, 3, 4, 7, 8]
