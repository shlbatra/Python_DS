class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        Start with boundaries in reverse. 
        2 loops one first and last row -> pacific and atlantic 
        first and last column - pacific and atlantic
        Run DFS on both adding to set if no border condition 
        or height less than prev ht. (Inc ht order as travel from water)
        Then intersection of both sets give points reqd for 
        reaching atlantic and pacific ocean 
        '''
        R,C=len(heights),len(heights[0])
        pac,atl=set(),set()
        
        def dfs(r,c,visit,prevHeight):
            if ((r,c) in visit or 
                r < 0 or c < 0 or r == R or c == C or 
                heights[r][c] < prevHeight):
                return 
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
            
        
        for c in range(C):
            dfs(0,c,pac,heights[0][c]) #Top col
            dfs(R-1,c,atl,heights[R-1][c]) #Bottom col
            
        for r in range(R):
            dfs(r,0,pac,heights[r][0]) #Top row
            dfs(r,C-1,atl,heights[r][C-1]) #Bottom row
        
        res=[]
        for i in range(R):
            for j in range(C):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])
                    
        return res
                