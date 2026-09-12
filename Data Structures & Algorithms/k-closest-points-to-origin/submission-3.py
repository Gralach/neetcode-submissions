class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x,y in points:
            distance = ((x)**2 + (y)**2)**0.5
            distances.append((distance, [x,y]))

        def sort(arr, s, e):
            if e - s +1 <= 1:
                return arr
            m = (s + e) // 2

            sort(arr, s, m)
            sort(arr, m+1, e)

            merge(arr, s, m ,e)
            
            return arr

        def merge(arr, s, m ,e):
            L = arr[s: m+1]
            R = arr[m+1 : e+1]

            i, j, k = 0, 0 ,s

            while i < len(L) and j < len(R):
                if L[i][0] <= R[j][0]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j+= 1
                k += 1
            
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
        temp = sort(distances, 0, len(distances))
        cur, res = 0, []
        while k:
            res.append(temp[cur][1])
            cur += 1
            k -= 1
        return res