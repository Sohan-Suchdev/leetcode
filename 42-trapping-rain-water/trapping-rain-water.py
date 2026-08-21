class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        ret = 0
        lMax = [0]*len(height)
        rMax = [0]*len(height)
        for i in range(1, len(height)):
            lMax[i] = max(lMax[i-1], height[i-1])
        for i in range(len(height)-2,-1,-1):
            rMax[i] = max(rMax[i+1], height[i+1])
        for i in range(1,len(height)-1):
            t = min(lMax[i], rMax[i]) - height[i]
            t = max(t,0)
            ret += t
        return ret

        