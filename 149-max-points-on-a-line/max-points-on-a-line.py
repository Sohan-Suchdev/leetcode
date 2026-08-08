import math
from collections import defaultdict

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        if len(points) <= 2:
            return len(points)
            
        max_total_points = 0
        
        for i in range(len(points)):
            x1, y1 = points[i]
            slope_counts = defaultdict(int)
            
            current_max = 1
            
            for j in range(len(points)):
                if i == j:
                    continue 
                    
                x2, y2 = points[j]
                
                dx = x2 - x1
                dy = y2 - y1
                
                gcd = math.gcd(dx, dy)
                
                dx //= gcd
                dy //= gcd
                
                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy
                    
                slope = (dy, dx)
                
                slope_counts[slope] += 1
                
                current_max = max(current_max, slope_counts[slope] + 1)
                
            max_total_points = max(max_total_points, current_max)
            
        return max_total_points