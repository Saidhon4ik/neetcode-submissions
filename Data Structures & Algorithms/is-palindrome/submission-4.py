class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)<0: return False
        res = ""
        for c in s:
            if c.isalnum():
                res+=c
        res = res.lower()
        return res == res[::-1]