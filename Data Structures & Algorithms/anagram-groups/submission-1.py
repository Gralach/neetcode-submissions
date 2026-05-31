class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for x in strs:
            temp = [0] * 26
            for i in x:
                temp[ord(i)-97] += 1
            anagram_dict[tuple(temp)].append(x)

        return [x for x in anagram_dict.values()]