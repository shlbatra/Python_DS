# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion_linear(self, n: int) -> int:
        for i in range(1,n+1):
            if isBadVersion(i):
                return i
        return n

    def firstBadVersion_binary(self, n: int) -> int:
        '''
        Sequence - 1, 2, 3, 4, 5   (Say 3 is bad)
        Use binary search - if get false then start update to mid+1
        if get true, then end update to mid-1
        Let the complete binary loop run through and return start+1 (First bad version)
        '''
        start=1
        end=n
        
        while start < end:
            mid= int((start+end)/2)
            if isBadVersion(mid) == True:
                end=mid-1
            elif isBadVersion(mid) == False:
                start=mid+1
            
        return start
