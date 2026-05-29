class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)<0: return False
        res = ""
        for c in s:
            res = "".join(char for char in s if char.isalnum())
        res = res.lower()
        return res == res[::-1]