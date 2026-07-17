class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        res = -float('inf')

        while l<r:
            res = max(res, min(height[l], height[r])*(r-l))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        
        return res
