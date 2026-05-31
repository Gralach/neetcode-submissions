class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1

        lefttemp = height[i]
        righttemp = height[j]
        
        water = 0
        while j > i:
            if height[i] < height[j]:
                i += 1
                lefttemp = max(lefttemp, height[i]) 
                print(lefttemp - height[i])
                water += lefttemp - height[i]
            elif height[i] >= height[j]:
                j -= 1
                righttemp = max(righttemp, height[j])
                print(righttemp - height[j])
                water += righttemp - height[j]
        return water