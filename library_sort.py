def library_sort(arr):
    sorted_arr = []
    while arr:
        smallest = min(arr)
        sorted_arr.append(smallest)
        arr.remove(smallest)
    return sorted_arr
  
  
  # Example Usage
  
arr = [4, 2, 7, 1, 3, 5, 6]
sorted_arr = library_sort(arr)
print(sorted_arr)
