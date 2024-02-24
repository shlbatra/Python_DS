class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        Use DFS to identify the size of each of the islands in the matrix
        Only run DFS when island value is 1 ; In DFS, return 0 in case not part 
        of island else sum 1 as part of island to area variable 
        Find max for each of the islands found
        '''
        visited_set=set()
        def dfs(i,j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]==0 or (i,j) in visited_set:
                return 0
            
            visited_set.add((i,j))
            area=dfs(i-1,j)
            area+=dfs(i,j-1)
            area+=dfs(i+1,j)
            area+=dfs(i,j+1)
            return 1+area
            
        area=0    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j]==1:
                    area=max(area,dfs(i,j))
        
        return area