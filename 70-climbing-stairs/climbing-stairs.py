class Solution:
    def climbStairs(self, n: int) -> int:
        choices = [1,2]
        for i in range(2,n):
            choices.append(choices[i-1]+choices[i-2])
        return choices[n-1]
