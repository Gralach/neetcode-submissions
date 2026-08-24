class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = ord("a")
        res = defaultdict(list)
        for string in strs:
            template = [0] * 26
            for char in string:
                template[a - ord(char)] += 1
            res[tuple(template)].append(string)
        return [values for key, values in res.items()]