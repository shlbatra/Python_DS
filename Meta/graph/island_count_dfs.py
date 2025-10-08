class IslandCountDFS:

    
    def dfs_island(self, grid, r, c, row, col, visited):
   
            
            if r >= 0 and c >= 0 and r < row and c < col:
                
                if (r, c) in visited:
                    return 0 
                visited.add((r, c)) # check for cycle

                if grid[r][c] == 'W': # check for water
                    return 0
                            
                self.dfs_island(grid, r-1, c, row, col, visited)
                self.dfs_island(grid, r+1, c, row, col, visited)
                self.dfs_island(grid, r, c-1, row, col, visited)
                self.dfs_island(grid, r, c+1, row, col, visited)
            
            return 1
                
    def island_count(self, grid):
        row, col = len(grid), len(grid[0])
        visited = set()
        num_islands = 0
        for r in range(0,row):
            for c in range(0,col):
                # print(r, c)
                # print(grid[r][c])
                num_islands += self.dfs_island(grid, r, c, row, col, visited)
        return num_islands
        
        
grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
]

# print(grid[5][5])

# print(len(grid), len(grid[0]))

dfs = IslandCountDFS()
ans = dfs.island_count(grid)  # 3
print(ans)