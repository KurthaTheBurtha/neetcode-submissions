class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = dict()
        for n in nums:
            cnts[n] = cnts.get(n, 0) + 1
        pairs = []
        for ke in cnts:
            tup = cnts[ke],ke
            pairs.append(tup)
        pairs.sort(reverse=True)
        key, v = zip(*pairs)
        v = list(v)
        return v[:k]
        
