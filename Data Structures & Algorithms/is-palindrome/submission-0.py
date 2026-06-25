class Solution:
    def isPalindrome(self, s: str) -> bool:
        phrase = ''.join([char for char in s if char.isalnum()])
        backwards = ""
        for i in range(len(s) - 1, -1, -1):
            backwards += s[i]
        backwards = ''.join([char for char in backwards if char.isalnum()])
        return phrase.lower() == backwards.lower()
        