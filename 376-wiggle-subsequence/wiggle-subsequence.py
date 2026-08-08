class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
            
        count = 1 
        prev_diff = 0
        
        for i in range(1, len(nums)):
            curr_diff = nums[i] - nums[i-1]
            
            if (curr_diff > 0 and prev_diff <= 0) or (curr_diff < 0 and prev_diff >= 0):
                count += 1
                prev_diff = curr_diff
                
        return count