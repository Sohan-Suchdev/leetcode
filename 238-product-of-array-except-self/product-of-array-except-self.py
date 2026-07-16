class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        left_products = [0] * n
        right_products = [0] * n
        result = [0] * n
        
        left_products[0] = 1
        for i in range(1, n):
            left_products[i] = left_products[i - 1] * nums[i - 1]
            
        right_products[n - 1] = 1
        for i in range(n - 2, -1, -1):
            right_products[i] = right_products[i + 1] * nums[i + 1]
            
        for i in range(n):
            result[i] = left_products[i] * right_products[i]
            
        return result