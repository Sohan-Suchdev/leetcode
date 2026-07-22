from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        
        for num in counts:
            if counts[num]>len(nums)//2:
                return num