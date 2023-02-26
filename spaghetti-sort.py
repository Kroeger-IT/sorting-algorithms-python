def spaghetti_sort(arr):
    n = len(arr)
    while n > 1:
        spaghetti = [[] for i in range(n)]
        for i in range(n):
            spaghetti[arr[i]].append(arr[i])
        arr = []
        for i in range(n - 1, -1, -1):
            if spaghetti[i]:
                arr += spaghetti[i]
        n = len(arr)
    return arr

# Example usage
arr = [4, 2, 1, 3, 0]
sorted_arr = spaghetti_sort(arr)
print(sorted_arr)
