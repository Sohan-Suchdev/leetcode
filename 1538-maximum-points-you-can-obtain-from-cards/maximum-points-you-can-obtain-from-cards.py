class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        curr_sum = sum(cardPoints[:k])
        max_sum = curr_sum
        
        n = len(cardPoints)

        for i in range(k):
            drop_left = cardPoints[k - 1 - i]
            pick_right = cardPoints[n - 1 - i]
            curr_sum = curr_sum - drop_left + pick_right
            
            if curr_sum > max_sum:
                max_sum = curr_sum
                
        return max_sum