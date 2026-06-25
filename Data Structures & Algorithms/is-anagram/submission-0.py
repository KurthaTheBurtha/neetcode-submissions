class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        D = {}
        for c in s:
            if d.get(c):
                d[c] += 1
            else:
                d[c] = 1
        for c in t:
            if D.get(c):
                D[c] += 1
            else:
                D[c] = 1
        
        for k in d:
            if not D.get(k):
                return False
            if d[k] != D[k]:
                return False
        for k in D:
            if not d.get(k):
                return False
            if d[k] != D[k]:
                return False
        return True