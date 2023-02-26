def bucket_sort(arr, bucket_size=5):
    if len(arr) == 0:
        return arr

    # Find minimum and maximum values in the array
    min_value, max_value = min(arr), max(arr)

    # Compute number of buckets and create an empty list for each bucket
    bucket_count = (max_value - min_value) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]

    # Assign each element to the appropriate bucket
    for i in range(len(arr)):
        bucket_index = (arr[i] - min_value) // bucket_size
        buckets[bucket_index].append(arr[i])

    # Sort each bucket and concatenate them into a single list
    sorted_arr = []
    for i in range(len(buckets)):
        sorted_bucket = sorted(buckets[i])
        sorted_arr.extend(sorted_bucket)

    return sorted_arr


# Example usage
arr = [3, 6, 1, 8, 4, 5]
sorted_arr = bucket_sort(arr)
print(sorted_arr)
