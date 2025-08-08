def longest_consecutive_sequence(nums):
    if not nums:
        return 0

    num_set = set(nums)
    longest_streak = 1

    for num in num_set:
        # Only check for the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            # Count the length of the sequence
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))  # Output: 4
print(longest_consecutive_sequence([0, 1, 2, 3, 4, 5]))  # Output: 6
print(longest_consecutive_sequence([4, 3, 55, 54, 2, 1, 7, 8, 53, 52, 56]))  # Output: 5
