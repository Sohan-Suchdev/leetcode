class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, curr, nums):
            if sum(curr)==target:
                res.append(curr.copy())
                return
            if sum(curr)>target:
                return
            if i == len(nums):
                return
            
            for j in range(i,len(nums)):
                curr.append(nums[j])
                backtrack(j, curr, nums)
                curr.pop()

        backtrack(0,[],nums)
        return res     
        
            
        