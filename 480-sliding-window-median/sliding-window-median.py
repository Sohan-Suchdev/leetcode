import heapq
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        small = [] 
        large = [] 
        invalid_counts = defaultdict(int) 
        ans = []
        
        for i in range(k):
            heapq.heappush(small, -nums[i])
            
        for _ in range(k // 2):
            heapq.heappush(large, -heapq.heappop(small))
            
        def get_median():
            if k % 2 == 1:
                return float(-small[0])
            else:
                return (-small[0] + large[0]) / 2.0
                
        ans.append(get_median())
        
        for i in range(k, len(nums)):
            out_num = nums[i - k]
            in_num = nums[i]
            balance = 0
            
            invalid_counts[out_num] += 1
            if out_num <= -small[0]:
                balance -= 1 
            else:
                balance += 1
                
            if small and in_num <= -small[0]:
                heapq.heappush(small, -in_num)
                balance += 1
            else:
                heapq.heappush(large, in_num)
                balance -= 1 
                
            if balance < 0: 
                heapq.heappush(small, -heapq.heappop(large))
            elif balance > 0:
                heapq.heappush(large, -heapq.heappop(small))
                
            while small and invalid_counts[-small[0]] > 0:
                invalid_counts[-small[0]] -= 1
                heapq.heappop(small)
                
            while large and invalid_counts[large[0]] > 0:
                invalid_counts[large[0]] -= 1
                heapq.heappop(large)
                
            ans.append(get_median())
            
        return ans