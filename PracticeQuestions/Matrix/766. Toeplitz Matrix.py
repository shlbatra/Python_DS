class Solution:
    def isToeplitzMatrix_v1(self, matrix: List[List[int]]) -> bool:
        '''
        Check mat[i][j]=mat[i-1][j-1]
        '''
        R=len(matrix)
        C=len(matrix[0])
        
        for i in range(R):
            for j in range(C):
                if i==0 or j==0:
                    continue
                else:
                    if matrix[i][j] != matrix[i-1][j-1]:
                        return False
        return True

    def isToeplitzMatrix_v2(self, matrix: List[List[int]]) -> bool:
        '''
        Check rowid-colid values for each cell with same difference are same
        '''
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                print(groups)
                if r-c not in groups:
                    groups[r-c] = val
                elif groups[r-c] != val:
                    return False
        return True