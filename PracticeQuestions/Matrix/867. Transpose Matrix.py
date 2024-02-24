class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        '''
        Create new matrix with reverse i and j and load from original matrix
        '''
        R = len(matrix)
        C = len(matrix[0])
        print(R)
        print(C)
        new_matrix = [[None]*R for _ in range(C)]
        print(new_matrix)
        for i in range(R):
            for j in range(C):
                new_matrix[j][i]=matrix[i][j]
        return new_matrix