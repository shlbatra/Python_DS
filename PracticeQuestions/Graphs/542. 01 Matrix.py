class Solution:
    def updateMatrix_dfs_unoptimized(self, mat: List[List[int]]) -> List[List[int]]:
        R,C=len(mat),len(mat[0])
        result=[[0]*C for i in range(R)]
        print(result)
        visited_set=set()

        def dfs(mat,i,j):
            if i<0 or j<0 or i>=R or j>=C or (i,j) in visited_set:
                return 100000
            if mat[i][j]==0:
                return 0
            visited_set.add((i,j))
            dist = 1 + min(dfs(mat,i-1,j),dfs(mat,i,j-1),dfs(mat,i+1,j),dfs(mat,i,j+1))
            visited_set.remove((i,j))
            return dist
        
        for i in range(R):
            for j in range(C):
                if mat[i][j]>0:
                    result[i][j]=dfs(mat,i,j)
        return result