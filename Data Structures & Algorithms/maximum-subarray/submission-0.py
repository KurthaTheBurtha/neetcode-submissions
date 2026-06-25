class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        maxsum = -9999999999999999
        for num in nums:
            sum += num
            if sum > maxsum:
                maxsum = sum
            if sum < 0:
                sum = 0
        return maxsum
            