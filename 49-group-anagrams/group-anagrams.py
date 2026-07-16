from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = defaultdict(list)
        
        for word in strs:
            count = [0] * 26
            
            for char in word:
                index = ord(char) - ord('a') 
                count[index] += 1
                
            h[tuple(count)].append(word)
            
        return list(h.values())