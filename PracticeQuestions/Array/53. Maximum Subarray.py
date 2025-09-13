import math

class Solution:
    def maxSubArray_badsolution(self, nums: List[int]) -> int:
        '''
        Use O(N2) solution. First loop start left end of subarray 
        Second loop right end of subarray
        Calculate sum and update the maxsum accordingly
        '''
        maxsum=nums[0]
        for i in range(len(nums)):
            cumsum = 0
            for j in range(i, len(nums)):
                cumsum += nums[j]
                maxsum = max(maxsum, cumsum)
        
        return maxsum

    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Use sliding window technique here. Keep cumsum as 0 
        Any time, cumsum < 0 , then update to 0 
        else store max of maxsum, cumsum as max value needed
        '''
        maxsum=nums[0]
        cumsum=0
        for i in range(len(nums)):
            if cumsum < 0:
                cumsum=0
            cumsum=cumsum+nums[i]
            maxsum=max(cumsum,maxsum)    
        return maxsum


    