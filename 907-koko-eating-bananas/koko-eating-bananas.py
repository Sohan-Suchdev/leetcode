class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        s = sum(piles)

        def isCorrect(num: int):
            if num<=h:
                return 0
            else:
                return 1
      
        while low <= high:
            mid = (low + high) // 2
            total_hours = sum(math.ceil(p / mid) for p in piles)

            if isCorrect(total_hours) == 0:
                high = mid - 1
            else:
                low = mid + 1

        return low