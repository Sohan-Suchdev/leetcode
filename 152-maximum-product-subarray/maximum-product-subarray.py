class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        prev_max = nums[0]
        prev_min = nums[0]
        res = nums[0]
        
        for num in nums[1:]:
            cand1 = num
            cand2 = num * prev_max
            cand3 = num * prev_min
            
            prev_max = max(cand1, cand2, cand3)
            prev_min = min(cand1, cand2, cand3)
            
            res = max(res, prev_max)
            
        return res