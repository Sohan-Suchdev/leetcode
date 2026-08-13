from collections import Counter

class Solution:
    def largestPalindromic(self, num: str) -> str:
        # Count and sort descending
        cnt = Counter(num)
        s_cnt = sorted(cnt.items(), reverse=True)

        odd = ''
        odd_flag = False
        ans = ''

        # Build the left side of the palindrome
        for x, y in s_cnt:
            if y % 2 == 1 and not odd_flag:
                odd_flag = True
                odd = x
            ans += x * (y // 2)

        # Manually remove leading zeros
        # If ans starts with '0', it means ONLY '0's were added to the left half.
        clean_ans = ""
        for char in ans:
            if clean_ans == "" and char == '0':
                continue # Skip leading zeros
            clean_ans += char
        ans = clean_ans

        # Construct final answer: Left half + Middle + Reversed Left half
        ans = ans + odd + ans[::-1]

        # If everything was stripped away, the only valid answer is '0'
        if ans == '':
            return '0'
            
        return ans