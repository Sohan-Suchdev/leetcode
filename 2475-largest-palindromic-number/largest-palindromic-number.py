from collections import Counter
class Solution:
    def largestPalindromic(self, num: str) -> str:
        cnt = Counter(num)
        s_cnt = sorted((cnt.items()), reverse = True)

        odd = ''
        odd_flag = False

        ans = ''
        for x, y in s_cnt:
            if y % 2 == 1 and not odd_flag:
                odd_flag = True
                odd = x
            ans += x*(y//2)

        ans = ans.lstrip('0')

        ans = ans + odd + ans[::-1]

        if ans == '':
            return '0'
        return ans