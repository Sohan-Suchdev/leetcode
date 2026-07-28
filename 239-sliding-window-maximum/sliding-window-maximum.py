import heapq as hq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = [(-nums[i], i) for i in range(k)]
        hq.heapify(max_heap)
        
        res = [-max_heap[0][0]]
        
        for i in range(k, len(nums)):
            hq.heappush(max_heap, (-nums[i], i))
            
            while max_heap[0][1] <= i - k:
                hq.heappop(max_heap)
                
            res.append(-max_heap[0][0])
            
        return res