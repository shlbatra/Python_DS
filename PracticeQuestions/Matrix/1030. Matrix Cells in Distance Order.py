class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        '''
        Create new matrix based on row and cols
        Use inbuilt sort function with key as the distance of each cell from cell provided
        '''
        newmat = [[i,j] for i in range(rows) for j in range(cols)]
        print(newmat)
        newmat.sort(key=lambda x: abs(x[0]-rCenter)+ abs(x[1]-cCenter))
        return newmat