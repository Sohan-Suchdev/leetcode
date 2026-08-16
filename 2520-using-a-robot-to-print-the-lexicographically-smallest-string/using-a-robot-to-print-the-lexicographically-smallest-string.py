class Solution:
    def robotWithString(self, s: str) -> str:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        stack = []
        result = []
        mn = 0  
        
        for c in s:
            count[ord(c) - ord('a')] -= 1
            stack.append(c)
            
            while mn < 26 and count[mn] == 0:
                mn += 1
            
            while stack and (mn == 26 or ord(stack[-1]) - ord('a') <= mn):
                result.append(stack.pop())
        
        while stack:
            result.append(stack.pop())
        
        return ''.join(result)
        