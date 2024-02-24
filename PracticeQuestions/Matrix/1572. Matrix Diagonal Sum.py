class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        '''
        Iterate through matrix and sum diagnol elements using logic 
        i==j for main diag
        i+j==R-1 for secondary diag
        '''
        R=len(mat)
        C=len(mat[0])
        res=0
        for i in range(R):
            for j in range(C):
                if i==j or (i+j==R-1):
                    print(mat[i][j])
                    res=res+mat[i][j]
            
        return res

    def diagonalSum_better(self, mat: List[List[int]]) -> int:
        '''
        Iterate through matrix over rows only
        i,i for main diag
        i,R-i-1 for secondary diag
        '''
        R=len(mat)
        res=0
        for i in range(R):
            res=res+mat[i][i]+mat[i][R-i-1]
        if R%2==1:
            res=res-mat[R//2][R//2]
            
        return res