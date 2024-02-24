class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        R = len(mat)
        C = len(mat[0])
        if R*C != r*c:
            return mat
        
        new_mat = [[None]*c for _ in range(r)]
        #Flatten original array
        temp=[]
        for i in range(R):
            for j in range(C):
                temp.append(mat[i][j])
        k=0        
        for i in range(r):
            for j in range(c):
                new_mat[i][j]=temp[k]
                k=k+1
        return new_mat

    def matrixReshape_v1(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        '''
         countcount back into 2-D matrix indices with a column count of cc, we can obtain the indices as res[count/c][count\%c]res[count/c][count%c] where count/ccount/c is the row number and count\%ccount%c is the coloumn number.
        '''
        R = len(mat)
        C = len(mat[0])
        if R*C != r*c:
            return mat
        
        new_mat = [[None]*c for _ in range(r)]
        
        k=0        
        for i in range(R):
            for j in range(C):
                new_mat[k//c][k%c]=mat[i][j]
                k=k+1
        return new_mat