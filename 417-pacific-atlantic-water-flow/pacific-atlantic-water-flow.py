class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(r, c, visited_set, prev_height):
            if (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visited_set or heights[r][c] < prev_height):
                return
            
            visited_set.add((r, c))
            
            dfs(r + 1, c, visited_set, heights[r][c])
            dfs(r - 1, c, visited_set, heights[r][c]) 
            dfs(r, c + 1, visited_set, heights[r][c])
            dfs(r, c - 1, visited_set, heights[r][c])             

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])           
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c]) 
            
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])       
            dfs(r, COLS - 1, atl, heights[r][COLS - 1]) 
        
        return [list(coord) for coord in (pac & atl)]