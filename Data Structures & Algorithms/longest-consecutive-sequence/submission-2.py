class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        longest = 0
        for num in hset:
            if (num - 1) not in hset:
                length = 1
                number = num
                while number + 1 in hset:
                    number += 1
                    length += 1
                longest = max(length, longest)
        return longest