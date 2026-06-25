class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: return len(s)
        left = 0
        right = 0
        longestlen = 0
        cnts = [0] * 128
        # cnts[ord(s[left])] += 1
        while right < len(s):
            c = s[right]
            cnts[ord(c)] += 1
            # non repeating
            # repeating
            while cnts[ord(c)] > 1:
                cnts[ord(s[left])] -= 1
                left += 1

            longestlen = max(longestlen, right - left + 1)
            right += 1

        return longestlen
        