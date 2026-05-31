class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1

        total = 0

        leftmax = height[i]
        rightmax = height[j]

        while i < j:
            if height[i] > height[j]:
                j -= 1
                rightmax = max(rightmax, height[j])
                total+= rightmax - height[j]
                print(total, "right")
            else:
                i+=1
                leftmax = max(leftmax, height[i])
                total+= leftmax - height[i]
                print(total, "left")
        return total