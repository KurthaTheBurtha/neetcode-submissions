class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [0] * 2001
        for num in nums:
            buckets[num + 1000] += 1
        topKFreq = []
        for i in range(k):
            topKFreq.append(buckets.index(max(buckets)) - 1000)
            buckets[buckets.index(max(buckets))] = 0
        return topKFreq 
        