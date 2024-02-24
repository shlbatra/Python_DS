class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        '''
        Calculate rowsum and colsum in one iteration using seperate lists for rowsum and colsum
        Check if cell is 1 and rowsum and colsum for that cell is 1 then increment count
        '''
        R=len(mat)
        C=len(mat[0])
        srows=[0]*R
        scols=[0]*C
        for i in range(R):
            for j in range(C):
                if mat[i][j]==1:
                    srows[i]+=1
                    scols[j]+=1
        count=0
        for i in range(R):
            for j in range(C):
                if mat[i][j]==1 and srows[i]==1 and scols[j]==1:
                    count+=1
        return count