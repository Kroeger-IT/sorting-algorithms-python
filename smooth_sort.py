def sift_down(arr, start, end, gaps):
    gap_idx = len(gaps) - 1
    while gap_idx >= 0:
        gap = gaps[gap_idx]
        i = start + gap
        j = start
        while i <= end:
            if arr[j] > arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
                if gap == 1:
                    i = j
                else:
                    i, j = j - gap, j
            i += gap
            j += gap
        gap_idx -= 1

def smooth_sort(arr):
    n = len(arr)
    gaps = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]
    while gaps and gaps[-1] >= n:
        gaps.pop()
    i = 1
    while i < n:
        if i + 1 < n and arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        sift_down(arr, 0, i, gaps)
        i += 1
    while i > 1:
        i -= 1
        sift_down(arr, 0, i, gaps)

# Example usage
arr = [5, 2, 8, 3, 9, 1]
smooth_sort(arr)
print(arr)
