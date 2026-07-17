class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = -float('inf')

        for r in range(1,len(prices)):
            res = max(res, prices[r]-prices[l])
            if prices[r] < prices[l]:
                l = r
        return max(0,res)

            
