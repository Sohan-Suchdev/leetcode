class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0
        for r in range(1,len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                res = max(res, prices[r] - prices[l])
        return res

            
