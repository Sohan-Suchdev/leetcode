class Solution:
    def minTaps(self, n: int, ranges: list[int]) -> int:
        max_reach = [0] * (n + 1)
        
        for i, radius in enumerate(ranges):
            if radius == 0:
                continue
                
            start = max(0, i - radius)
            end = min(n, i + radius)
            
            max_reach[start] = max(max_reach[start], end)
            
        taps = 0
        current_end = 0
        farthest_next = 0
        
        for i in range(n):
            farthest_next = max(farthest_next, max_reach[i])
            
            if i == current_end:
                if farthest_next <= i:
                    return -1
                
                taps += 1
                current_end = farthest_next
                
        return taps