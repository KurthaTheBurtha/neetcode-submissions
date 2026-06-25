class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for num in nums:
            if d.get(num) and d[num] > 0:
                return True
            else:
                d[num] = 1
        return False
