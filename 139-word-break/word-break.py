class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(1, len(s) + 1):
            for word in wordDict:
                word_len = len(word)
                if i - word_len >= 0 and dp[i - word_len] and s[i - word_len:i] == word:
                    dp[i] = True
                    break
                    
        return dp[-1]