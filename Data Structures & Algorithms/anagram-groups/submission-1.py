class Solution:
    def getCounts(self, word):
        counts = {}
        for c in word:
            if counts.get(c):
                counts[c] += 1
            else:
                counts[c] = 1
        return counts
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dict: {dict, list}
        # for all strings
            # if in dict
                # add to dict
            # if not
                # count characters
                # add to dict
                # add to list
        # convert dict to list
        words = {}
        for word in strs:
            counts = tuple(sorted(self.getCounts(word).items()))
            if counts in words:
                words[counts].append(word)
            else:
                words[counts] = [word]
        print(words)
        final = []
        for key in words:
            final.append(words[key])
        return final

