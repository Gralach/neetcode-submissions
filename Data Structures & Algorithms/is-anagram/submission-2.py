class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_dict = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i not in anagram_dict:
                anagram_dict[i] = 1
            else:
                anagram_dict[i] += 1

        for i in t:
            if i in anagram_dict:
                anagram_dict[i] -= 1
                if anagram_dict[i] < 0:
                    return False
            else:
                return False
        return True
            
        