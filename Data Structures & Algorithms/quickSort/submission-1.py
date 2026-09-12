# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def sort(arr, s, e):
            # base case
            if e-s + 1 <= 1:
                return arr
            
            # variables
            pivot = arr[e] # naive -> takes the end
            x = s # pointer

            for i in range(s, e):
                if arr[i].key < pivot.key:
                    temp = arr[x]
                    arr[x] = arr[i]
                    arr[i] = temp
                    x += 1

            # always move pivot to end of left side
            # x will always be on end of left
            temp = arr[x]
            arr[x] = arr[e] 
            arr[e] = temp

            # recursive
            sort(arr, s, x-1) # not including pivot
            sort(arr, x+1, e)

            return arr
        return sort(pairs, 0, len(pairs)-1)

