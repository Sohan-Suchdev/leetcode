from collections import Counter
import heapq as hq

class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        max_heap = []
        
        for letter, count in counts.items():
            if count > (len(s) + 1) // 2:
                return ""
            hq.heappush(max_heap, (-count, letter))
        
        res = [] 
        
        while len(max_heap) > 1:
            freq1, letter1 = hq.heappop(max_heap)
            freq2, letter2 = hq.heappop(max_heap)
            
            res.append(letter1)
            res.append(letter2)
            
            freq1 += 1
            freq2 += 1
            
            if freq1 != 0:
                hq.heappush(max_heap, (freq1, letter1))
            if freq2 != 0:
                hq.heappush(max_heap, (freq2, letter2))
        
        if max_heap:
            freq, letter = hq.heappop(max_heap)
            res.append(letter)
            
        return "".join(res)