# Define the introsort function
def introsort(arr):
    # Set the maximum depth of recursion for introsort
    max_depth = 2 * (len(arr).bit_length())

    # Define the partition function
    def partition(start, end):
        pivot_index = start
        pivot_value = arr[end]
        for i in range(start, end):
            if arr[i] < pivot_value:
                arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
                pivot_index += 1
        arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
        return pivot_index

    # Define the quicksort function
    def quicksort(start, end, depth):
        if end - start < 16:
            arr[start:end+1] = sorted(arr[start:end+1])
        elif depth == 0:
            heap_sort(start, end)
        else:
            pivot_index = partition(start, end)
            quicksort(start, pivot_index-1, depth-1)
            quicksort(pivot_index+1, end, depth-1)

    # Define the heapsort function
    def heap_sort(start, end):
        def sift_down(start, end):
            root = start
            while True:
                child = 2 * root + 1
                if child > end:
                    break
                if child + 1 <= end and arr[child] < arr[child+1]:
                    child += 1
                if arr[root] < arr[child]:
                    arr[root], arr[child] = arr[child], arr[root]
                    root = child
                else:
                    break

        for i in range(end, start-1, -1):
            arr[start], arr[i] = arr[i], arr[start]
            sift_down(start, i-1)

    # Call the quicksort function
    quicksort(0, len(arr)-1, max_depth)
    
    
# Example Usage
    
arr = [5, 7, 1, 9, 2, 8, 4, 3, 6, 0]
print("Unsorted array:", arr)
introsort(arr)
print("Sorted array:", arr)
