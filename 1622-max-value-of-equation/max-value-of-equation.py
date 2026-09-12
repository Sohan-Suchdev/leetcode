from collections import deque

class Solution:
    def findMaxValueOfEquation(self, points: list[list[int]], k: int) -> int:
        dq = deque()  # Stores tuples of (y - x, x)
        max_val = float('-inf')
        
        for x, y in points:
            while dq and x - dq[0][1] > k:
                dq.popleft()
                
            if dq:
                max_val = max(max_val, dq[0][0] + y + x)

            curr_val = y - x
            while dq and dq[-1][0] <= curr_val:
                dq.pop()
                
            dq.append((curr_val, x))
            
        return max_val