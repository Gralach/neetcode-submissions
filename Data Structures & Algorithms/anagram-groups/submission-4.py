class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = defaultdict(list)
        for str in strs:
            temp = [0] * 26
            # print(temp)
            for i in str:
                temp[ord(i) - ord("a")] += 1
            check[tuple(temp)].append(str)
        res = []
        for k, v in check.items():
            res.append(v)
        return res