import collections
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, price in flights:
            adj[u].append((v, price))
            
        min_cost = [float('inf')] * n
        min_cost[src] = 0
        
        queue = collections.deque([(src, 0)])
        stops = 0
        
        while queue and stops <= k:
            for _ in range(len(queue)):
                curr_node, curr_cost = queue.popleft()
                
                for neighbor, price in adj[curr_node]:
                    next_cost = curr_cost + price
                    
                    if next_cost < min_cost[neighbor]:
                        min_cost[neighbor] = next_cost
                        queue.append((neighbor, next_cost))
            
            stops += 1
            
        return min_cost[dst] if min_cost[dst] != float('inf') else -1