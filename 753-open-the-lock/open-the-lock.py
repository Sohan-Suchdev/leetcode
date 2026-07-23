from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)      
        if "0000" in visited:
            return -1
            
        queue = deque([("0000", 0)])
        visited.add("0000")
        
        while queue:
            state, turns = queue.popleft()
            if state == target:
                return turns
                
            for i in range(4):
                digit = int(state[i])
                
                up = str((digit + 1) % 10)
                down = str((digit - 1) % 10)
                
                state_up = state[:i] + up + state[i+1:]
                state_down = state[:i] + down + state[i+1:]
                
                for next_state in (state_up, state_down):
                    if next_state not in visited:
                        visited.add(next_state)
                        queue.append((next_state, turns + 1))
                        
        return -1