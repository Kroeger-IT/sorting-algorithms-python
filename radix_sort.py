def radix_sort(nums):
    RADIX = 10
    max_length = False
    tmp, placement = -1, 1

    while not max_length:
        max_length = True
        # declare and initialize buckets
        buckets = [list() for _ in range(RADIX)]

        # split nums between lists
        for i in nums:
            tmp = i // placement
            buckets[tmp % RADIX].append(i)
            if max_length and tmp > 0:
                max_length = False

        # empty lists into nums array
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                nums[a] = i
                a += 1

        # move to next digit
        placement *= RADIX
    return nums

# example usage
nums = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_nums = radix_sort(nums)
print(sorted_nums)
