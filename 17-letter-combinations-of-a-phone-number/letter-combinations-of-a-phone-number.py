class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        d = {"2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]}

        res = []

        def dfs(i: int, curStr: str):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
                
            for char in d[digits[i]]:
                dfs(i + 1, curStr + char)
                
        dfs(0, "")
        
        return res
        