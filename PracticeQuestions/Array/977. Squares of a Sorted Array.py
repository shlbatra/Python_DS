class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''
        Use two pointer approach left and right
        If left > right, add right^2 else left^2 -? Finally return the reverse of the result
        '''
        res=[]
        l=0
        r=len(nums)-1
        while l<=r:
            if abs(nums[l])>=abs(nums[r]):
                res.append(nums[l]**2)
                l=l+1
            else:
                res.append(nums[r]**2)
                r=r-1
        return res[::-1]

    def sortedSquares_badsolution(self, nums: List[int]) -> List[int]:
        '''
        First get the squared list and then sort the list - Solution would be O(nlogn)
        '''
        res=[]
        for i in range(len(nums)):
            res.append(nums[i]**2)
         
        return sorted(res)