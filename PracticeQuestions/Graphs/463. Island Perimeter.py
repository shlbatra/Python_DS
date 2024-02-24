class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        '''
        Start at any island that is land and then run DFS to add boundary (+1) if the next neigbour is a boundary or 
        water. Also keep a visited set so as to not take that into account once you process that grid
        '''
        visited=set()
        def dfs(i,j):
            if (i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]==0):
                return 1
            if (i,j) in visited:
                return 0

            visited.add((i,j))
            perim=dfs(i,j+1)
            perim+=dfs(i+1,j)
            perim+=dfs(i,j-1)
            perim+=dfs(i-1,j)
            return perim
                    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return dfs(i,j)