import heapq
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = [-g for g in gifts]
        heapq.heapify(max_heap)

        for _ in range(k):
            m = -heapq.heappop(max_heap)
            heapq.heappush(max_heap, -math.isqrt(m))
        return -sum(max_heap)