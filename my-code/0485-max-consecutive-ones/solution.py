class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        temp_max = 0
        for num in nums:
            if num == 1:
                temp_max += 1
            else:
                temp_max = 0
            
            if temp_max>max:
                max = temp_max
            
        return max
