def cycle_sort(array):
    n = len(array)
    for cycle_start in range(0, n - 1):
        item = array[cycle_start]
        pos = cycle_start
        for i in range(cycle_start + 1, n):
            if array[i] < item:
                pos += 1
        if pos == cycle_start:
            continue
        while item == array[pos]:
            pos += 1
        array[pos], item = item, array[pos]
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, n):
                if array[i] < item:
                    pos += 1
            while item == array[pos]:
                pos += 1
            array[pos], item = item, array[pos]
    return array

  
  #Example Usage
  
array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
sorted_array = cycle_sort(array)
print(sorted_array)
