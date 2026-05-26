class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, curr, nums):
            if i == len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[i])

            backtrack(i + 1, curr, nums)

            curr.pop()

            backtrack(i + 1, curr, nums)

        backtrack(0, [], nums)

        return res   
