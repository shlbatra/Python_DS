class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        '''
        Initial get rowmins for all rows and store in set
        Next another iteration check for colmax and if that is in rowmins - it is the answer
        '''
        R=len(matrix)
        C=len(matrix[0])
        result=[]
        rowmin=set()
        for i in range(R):
            temp_min=float('inf')
            for j in range(C):
                if matrix[i][j]<temp_min:
                    temp_min=matrix[i][j]
            rowmin.add(temp_min)
        print(rowmin)
        for i in range(C):
            temp_max=0
            for j in range(R):
                if matrix[j][i]>temp_max:
                    temp_max=matrix[j][i]
            print(temp_max)
            if temp_max in rowmin:  #O(1)
                result.append(temp_max)
        
        return result 