class Solution:
    def trap(self, height: List[int]) -> int:
        l , r = 0, len(height) - 1
        trapped = 0
        maxl, maxr = height[l], height[r]

        while l < r:
            if height[l] >= height[r]:
                r-=1
                maxr = max(maxr, height[r])
                trapped += maxr-height[r]
            if height[r] > height[l]:
                l+=1
                maxl = max(height[l], maxl)
                trapped += maxl-height[l]
        return(trapped)
        