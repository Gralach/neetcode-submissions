class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        water = 0

        leftmax = height[i]
        rightmax = height[j]

        while i < j:
            if height[i] < height[j]:
                i += 1
                leftmax = max(height[i], leftmax)
                water += leftmax - height[i]
            else:
                j -= 1
                rightmax = max(height[j], rightmax)
                water += rightmax - height[j]
        return water