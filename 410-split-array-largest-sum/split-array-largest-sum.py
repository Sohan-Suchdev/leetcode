from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(target: int) -> bool:
            subarrays = 1
            current_sum = 0
            
            for num in nums:
                if current_sum + num > target:
                    subarrays += 1
                    current_sum = num  
                    
                    if subarrays > k:
                        return False
                else:
                    current_sum += num
                    
            return True

        left = max(nums) 
        right = sum(nums)  
        best_min_largest_sum = right
        
        while left <= right:
            mid = (left + right) // 2
            
            if can_split(mid):
                best_min_largest_sum = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return best_min_largest_sum