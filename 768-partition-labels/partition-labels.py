from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_seen = {}
        for i, char in enumerate(s):
            last_seen[char] = i
            
        result = []
        start = 0
        end = 0
        
        for i, char in enumerate(s):
            end = max(end, last_seen[char])
            
            if i == end:
                result.append(i - start + 1)
                start = i + 1
                
        return result