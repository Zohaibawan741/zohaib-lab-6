def longestConsecutive(nums):
    if not nums:
        return 0

    num_set = set(nums)
    longest_sequence = 0

    for num in num_set:
        if num - 1 not in num_set: 
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_sequence = max(longest_sequence, current_streak)

    return longest_sequence

nums = [100, 4, 200, 1, 3, 2]
result = longestConsecutive(nums)
print(result)