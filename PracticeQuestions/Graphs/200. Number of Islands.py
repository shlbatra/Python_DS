from matplotlib import collections


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        '''
        Use DFS to identify the size of each of the islands in the matrix
        Only run DFS when island value is 1 ; In DFS, return 0 in case not part 
        of island else 1 if part of island only once 
        Keep a track of sum of all islands as visited set will make sure we 
        visit each cell only once
        '''
        if not grid:
            return 0
        visited_set=set()
        ROWS,COLS=len(grid),len(grid[0])
        
        def dfs(r,c):
            if r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c]=="0" or (r,c) in visited_set:
                return 0
            visited_set.add((r,c))
            
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
            return 1
        
        count=0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]=="1":
                    count+=dfs(i,j)
        return count

    
    def numIslands_BFS(self, grid: List[List[str]]) -> int:
        '''
        Use BFS to identify the size of each of the islands in the matrix
        Only run BFS when island value is 1 ; In BFS, return 1 after iterating 
        through entire part of island with all consecutive 1s. 
        Keep a track of sum of all islands as visited set will make sure we 
        visit each cell only once
        '''
        if not grid:
            return 0
        visited_set=set()
        ROWS,COLS=len(grid),len(grid[0])

        def bfs(i,j):
            q= collections.deque()
            visited_set.add((i,j))
            q.append((i,j))
            while q:
                row,col=q.popleft()  # Pop first so BFS, If pop last element then DFS
                directions = [[1,0],[-1,0],[0,1],[0,-1]]

                for dr,dc in directions:
                    r,c= row+dr, col+dc
                    if (r in range(ROWS) and 
                       c in range(COLS) and 
                       (r,c) not in visited_set and 
                       grid[r][c] == "1"):
                       q.append((r,c))
                       visited_set.add((r,c))
            return 1


        count=0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]=="1" and (i,j) not in visited_set:
                    count+=bfs(i,j)
        return count