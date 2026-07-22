from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts = Counter(arr1)
        res = []

        for num in arr2:
            res += [num] * counts.pop(num)
        
        for num in sorted(counts):
            res += [num] * counts[num]
        
        return res
        