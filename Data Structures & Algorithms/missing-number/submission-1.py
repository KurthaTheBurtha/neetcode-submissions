class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numset = set(range(len(nums) + 1))
        for n in nums:
            numset.remove(n)
        return numset.pop()
    

            