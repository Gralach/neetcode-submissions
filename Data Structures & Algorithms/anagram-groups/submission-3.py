class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        start = ord("a")
        for string in strs:
            check = [0]*26
            for char in string:
                check[ord(char)-start] += 1
            res[tuple(check)].append(string)
        result = []
        for key, value in res.items():
            result.append(value)
        return result