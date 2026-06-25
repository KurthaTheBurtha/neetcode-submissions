class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1cnts = dict()
        alpha = "abcdefghijklmnopqrstuvwxyz"
        for l in alpha:
            s1cnts[l] = 0
        for c in s1:
            s1cnts[c] = s1cnts.get(c, 0) + 1
        k = len(s1)

        s2cnts = dict()
        for l in alpha:
            s2cnts[l] = 0
        start = s2[0:k]
        for c in start:
            s2cnts[c] = s2cnts.get(c, 0) + 1

        if s1cnts == s2cnts:
            return True
        for i in range(len(s2) -  k):
            # add cnt
            s2cnts[s2[i + k]] = s2cnts.get(s2[i + k], 0) + 1
            # subtract previous  one
            s2cnts[s2[i]] = s2cnts.get(s2[i], 0) - 1
            # check if sets match
            print(s1cnts)
            print(s2cnts)
            print("\n")
            if s1cnts == s2cnts:
                return True
        if s1cnts == s2cnts:
            return True
        return False
        
        