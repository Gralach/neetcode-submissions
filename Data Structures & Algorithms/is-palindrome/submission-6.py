class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ""
        for x in s:
            if x.isalnum():
                text += x.lower()
        if text == text[::-1]:
            return True
        return False