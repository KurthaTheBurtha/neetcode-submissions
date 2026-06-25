class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue  # skip duplicate i values
            
            target = -1 * nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                pair = nums[l] + nums[r]
                if pair == target:
                    res.append([nums[l], nums[i], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1  # skip duplicate l values
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1  # skip duplicate r values
                elif pair < target:
                    l += 1
                else:
                    r -= 1
        return res