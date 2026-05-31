class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        max = 0

        while r > l:
            water = min(heights[l], heights[r]) * (r-l)
            if max < water:
                max = water
            if heights[l] > heights[r]:
                r-=1
            elif heights[l] <= heights[r]:
                l+=1
        return max