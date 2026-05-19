class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in bracket_map:
                top_element = stack.pop() if stack else '#'
                if bracket_map[c] != top_element:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0
        
