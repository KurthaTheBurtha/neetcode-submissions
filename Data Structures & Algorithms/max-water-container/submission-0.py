class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        l = 0
        r = len(heights) - 1
        # min (l, r) * r - l
        while (l < r):
            area = min(heights[l], heights[r]) * (r-l)
            if (area > maxarea):
                maxarea = area;
            if (heights[l] >= heights[r]):
                r -= 1
            else:
                l += 1
        return maxarea
