class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        while l <= r:
            while l <= r and not (s[l].isalpha() or s[l].isdigit()):
                l += 1
            while l <= r and not (s[r].isalpha() or s[r].isdigit()):
                r -= 1
            if l <= r and s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True