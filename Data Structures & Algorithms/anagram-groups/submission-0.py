class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for i in strs:
            count = [0] * 26
            for chars in i:
                count[ord(chars) - ord("a")]+= 1
            result[tuple(count)].append(i)
        return result.values()

