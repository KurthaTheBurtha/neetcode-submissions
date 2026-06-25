class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        valid = 'abcdefghijklmnopqrstuvwxyz1234567890'
        news = ''
        for c in s:
            if c in valid:
                news += c
        s = news
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]: return False
            l += 1
            r -= 1
        return True