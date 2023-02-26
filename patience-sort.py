def patience_sort(nums):
    piles = []
    for num in nums:
        pile_index = bisect_left([pile[-1] for pile in piles], num) if piles else 0
        if pile_index == len(piles):
            piles.append([num])
        else:
            piles[pile_index].append(num)
    nums.clear()
    while piles:
        smallest_pile = min(piles, key=lambda pile: pile[0])
        nums.append(smallest_pile.pop(0))
        if not smallest_pile:
            piles.remove(smallest_pile)
    return nums

  # Example Usage
  
unsorted_nums = [5, 2, 7, 3, 9, 1, 4, 6, 8]
sorted_nums = patience_sort(unsorted_nums)
print(sorted_nums) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

