class Solution:
    def maxLength(self, arr: List[str]) -> int:
        valid_arr = [word for word in arr if len(word) == len(set(word))]
        
        def dfs(index: int, current_set: set) -> int:
            if index == len(valid_arr):
                return len(current_set)
            
            max_len = dfs(index + 1, current_set)
            
            word_set = set(valid_arr[index])
            
            if not (current_set & word_set):
                take_len = dfs(index + 1, current_set | word_set)
                
                max_len = max(max_len, take_len)
                
            return max_len

        return dfs(0, set()) 