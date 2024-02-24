class Solution:

    def setZeroes_CheckAgain(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R=len(matrix)
        C=len(matrix[0])
        matrix_copy = [x[:] for x in matrix]
        #determine which rows/cols need to be zero
        for r in range(R):
            for c in range(C):
                if matrix[r][c]==0:
                    print(matrix_copy[:][c])
                    print(matrix_copy[r][:])
                    #Set row to 0
                    matrix_copy[:][c]=[0]*R
                    #Set col to 0
                    matrix_copy[r][:]=[0]*C
                        
        return matrix_copy


    def setZeroes_v1(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R=len(matrix)
        C=len(matrix[0])
        rows,cols=set(),set()
        #determine which rows/cols need to be zero
        for r in range(R):
            for c in range(C):
                if matrix[r][c]==0:
                    rows.add(r)
                    cols.add(c)
           
        for r in range(R):
            for c in range(C):
                if r in rows or c in cols:
                    matrix[r][c]=0


    def setZeroes_v2(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R=len(matrix)
        C=len(matrix[0])
        rowZero=False
        #determine which rows/cols need to be zero
        for r in range(R):
            for c in range(C):
                if matrix[r][c]==0:
                    #Set row to 0
                    matrix[0][c]=0
                    if r>0:
                        #Set col to 0
                        matrix[r][0]=0
                    else:
                        rowZero=True
                        
        for r in range(1,R):
            for c in range(1,C):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c]=0
        #Update col 0 if 0            
        if matrix[0][0]==0:
            for r in range(R):
                matrix[r][0]=0
        #Update row 0 if 0
        if rowZero==True:
            for c in range(C):
                matrix[0][c]=0

mat = [[1,1,1],[1,0,1],[1,1,1]]
print(mat)
s=Solution()
s.setZeroes_v2(mat)
print(mat)