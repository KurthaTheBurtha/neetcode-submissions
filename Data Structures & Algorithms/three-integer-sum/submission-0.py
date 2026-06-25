class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = set()
        for i in range(len(nums)):
            l = 0
            r = len(nums) - 1
            while l < i and i < r:
                if nums[l] + nums[r] == (-1) * nums[i]:
                    ans.add((nums[l],nums[i],nums[r]))
                    l += 1
                elif nums[l] + nums[r] < (-1) * nums[i]:
                    l += 1
                elif nums[l] + nums[r] > (-1) * nums[i]:
                    r -= 1
        return list(ans)
