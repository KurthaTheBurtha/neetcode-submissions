class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = []
        for r in matrix:
            nums = nums + r
        l = 0
        r = len(nums)
        while l < r:
            mid = (l + r) // 2
            if target < nums[mid]:
                r = mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                return True
        return False   
