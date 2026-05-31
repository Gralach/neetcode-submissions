class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0 , len(height) - 1
        maxi, maxj = height[i], height[j]
        trapped = 0
        while i < j:
            if height[i] < height[j]:
                i += 1
                maxi = max(height[i], maxi)
                trapped += maxi - height[i]
            else:
                j -= 1
                maxj = max(height[j], maxj)
                trapped += maxj - height[j]
            print(i, j)
            print(trapped)
        return trapped