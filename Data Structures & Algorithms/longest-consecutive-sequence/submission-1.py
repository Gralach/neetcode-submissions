def quickSort(arr):
    # strictly use bigger and lower than to remove duplicates
        if len(arr) > 1:
            pivot = arr[0]
            left = []
            right = []
            for i in range(1, len(arr), 1):
                if arr[i] > pivot:
                    right.append(arr[i])
                if arr[i] < pivot:
                    left.append(arr[i])
            return quickSort(left) + [pivot] + quickSort(right)
        else:
            return arr

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        sort = quickSort(nums)
        curlongest, maxlongest = 1, 1
        print(sort)
        
        for i in range(1, len(sort), 1):
            if sort[i] == sort[i-1] + 1:
                curlongest += 1
            else:
                maxlongest = max(maxlongest,curlongest)
                curlongest = 1
        
        maxlongest = max(maxlongest,curlongest)
        return maxlongest
        