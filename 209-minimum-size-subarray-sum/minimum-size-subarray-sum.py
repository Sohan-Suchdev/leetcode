class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:      
        l = 0
        min_len = float('inf')
        current_sum = 0

        for r in range(len(nums)):
            current_sum += nums[r]
            while current_sum>=target:
                min_len = min(min_len, r - l + 1)
                current_sum -= nums[l]
                l+=1
                
        
        if min_len!=float('inf'):
            return min_len
        else:
            return 0


        

        