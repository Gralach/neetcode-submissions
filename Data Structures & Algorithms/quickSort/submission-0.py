# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def sort(arr, s, e):
            # base case -> same as merge sort
            if e-s + 1 <= 1:
                return arr
            pivot = arr[e]
            k = s

            for i in range(s, e):
                if arr[i].key < pivot.key:
                    temp = arr[k]
                    arr[k] = arr[i]
                    arr[i] = temp
                    k += 1
            arr[e] = arr[k]
            arr[k] = pivot

            sort(arr, s, k-1)
            sort(arr, k + 1, e)
            
            return arr
        return sort(pairs, 0, len(pairs)-1)