import heapq
from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1 or k == len(weights):
            return 0
            
        min_heap = []  
        max_heap = [] 
        
        for i in range(len(weights) - 1):
            pair_sum = weights[i] + weights[i + 1]
            
            heapq.heappush(min_heap, pair_sum)
            if len(min_heap) > k - 1:
                heapq.heappop(min_heap)
                
            heapq.heappush(max_heap, -pair_sum)
            if len(max_heap) > k - 1:
                heapq.heappop(max_heap)
                
        max_score = sum(min_heap)
        min_score = -sum(max_heap)
        
        return max_score - min_score