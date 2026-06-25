class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        cnts = [0] * 26
        maxcnt = 0
        result = 0
        
        for r in range(len(s)):
            # iterate counts and maxcount
            i = ord(s[r]) - 65
            cnts[i] += 1
            maxcnt = max(maxcnt, cnts[i])
            # move l if invalid window size
            if (r - l + 1) > (k + maxcnt):
                j = ord(s[l]) - 65
                cnts[j] -= 1
                l += 1
            # check if k + maxcount is greater than result
            result = max(k + maxcnt, result)
        return min(result, len(s))
