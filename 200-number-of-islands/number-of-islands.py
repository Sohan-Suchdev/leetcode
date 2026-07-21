class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            ROWS, COLS = len(grid), len(grid[0])
            if (min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == "0"):
                return
            
            grid[r][c]="0"

            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
        
        islandCount = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    dfs(i ,j)
                    islandCount +=1

        return islandCount

              