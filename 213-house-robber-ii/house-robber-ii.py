from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def rob_linear(houses: List[int]) -> int:
            prev2 = 0
            prev1 = 0
            for num in houses:
                current = max(prev1, prev2 + num)
                prev2 = prev1
                prev1 = current
            return prev1
            
        skip_first = rob_linear(nums[1:])
        skip_last = rob_linear(nums[:-1])
        
        return max(skip_first, skip_last)