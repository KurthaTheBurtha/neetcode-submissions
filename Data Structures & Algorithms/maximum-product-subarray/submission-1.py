class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # two elements
        # check one, two, one * two
        # three elements
        # check one, two, three, one * two, one * three, two * three, one * two * three
        # max prod (two elements), 
        curMax = 1
        curMin = 1
        maxProduct = nums[0]
        for num in nums:
            tmp = curMax * num
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(tmp, num * curMin, num)
            maxProduct = max(maxProduct, curMax)
        return maxProduct

