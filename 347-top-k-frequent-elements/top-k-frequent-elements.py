from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        l = sorted(c, key=c.get, reverse=True)
        
        return l[:k]