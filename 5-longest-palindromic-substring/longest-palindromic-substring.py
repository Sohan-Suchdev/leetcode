class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        maxLen = 0

        def expand(l: int, r: int):
            nonlocal res, maxLen
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_len = r - l + 1
                if curr_len > maxLen:
                    maxLen = curr_len
                    res = s[l:r+1]
                l -= 1
                r += 1

        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)

        return res