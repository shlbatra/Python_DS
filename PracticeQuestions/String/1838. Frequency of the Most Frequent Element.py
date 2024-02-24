class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        '''
        Sort and Sliding Window - O(nlogn)
        k - limited budget to increment
        [1,1,1,2,2,4] -> Find values closest to 4 -> check left values that are closest
        Sliding Window 
        l and r pointer -> r most frequent value, and keep growing l to r till budget k
        
        Expand while 
        (num[r].windowLen <= Total+k) -> k budget to get to all values in window as same
        Find max size of windowLen to return
        '''
        nums = sorted(nums)
        l=0
        running_total,res=0,0
        for r in range(len(nums)):
            running_total+=nums[r]
            print(running_total)
            while nums[r]*(r-l+1) > running_total+k: # Window invalid then shrink
                   running_total -= nums[l]
                   l+=1
            res=max(res,(r-l+1))
        return res
        