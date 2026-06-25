class Solution:
    def countSubstrings(self, s: str) -> int:
        
        # all 1s
        cnt = len(s)
        for i in range(len(s)):
            l = i
            r = i
            while l >= 0 and r < len(s):
                l -= 1
                r += 1
                if l < 0 or r >= len(s):
                    break
                if s[l] != s[r]:
                    break
                print(s[l:r+1])
                cnt += 1
            l = i
            r = i + 1
            if r < len(s) and s[l] == s[r]:
                cnt += 1
                print(s[l:r+1])
                while l >= 0 and r < len(s):
                    l -= 1
                    r += 1
                    if l < 0 or r >= len(s):
                        break
                    if s[l] != s[r]:
                        break
                    print(s[l:r+1])
                    cnt += 1
        return cnt