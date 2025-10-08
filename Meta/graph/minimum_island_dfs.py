class MinimumIslandDFS:

    
    def dfs_island(self, grid, r, c, row, col, visited):

        if r >= 0 and c >= 0 and r < row and c < col:

            if (r, c) in visited: # check if already included this as part of island
                return 0
            visited.add((r,c))
 
            if grid[r][c] == "W": # check if water island
                return 0
            
            size = 1
            
            size += self.dfs_island(grid, r-1, c, row, col, visited) # Include current island as part of already growing island
            size += self.dfs_island(grid, r+1, c, row, col, visited)
            size += self.dfs_island(grid, r, c-1, row, col, visited)
            size += self.dfs_island(grid, r, c+1, row, col, visited)
        
            return size
        
        else:
            return 0

    def min_island(self, grid):
        visited = set()
        row, col = len(grid), len(grid[0])

        min_size = 99999
        for r in range(0, row):
            for c in range(0, col):
                size = self.dfs_island(grid, r, c, row, col, visited)
                if size > 0 and size < min_size:
                    min_size = size
        return min_size
        
grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
]


dfs = MinimumIslandDFS()
ans = dfs.min_island(grid)  # 2
print(ans)