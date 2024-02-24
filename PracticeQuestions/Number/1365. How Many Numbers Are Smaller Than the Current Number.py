# Given the array nums, for each nums[i] find out how many 
# numbers in the array are smaller than it. That is, for 
# each nums[i] you have to count the number of valid j's such 
# that j != i and nums[j] < nums[i].

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums,reverse=True) #O(nLogn)
        print(nums)
        smaller_count={}
        for i in range(len(sorted_nums)-1):    #O(n)
            if sorted_nums[i+1]<sorted_nums[i]:
                smaller_count[sorted_nums[i]]=len(nums) - i - 1 
        #if sorted_nums[i] != sorted_nums[len(sorted_nums)-1]:
        smaller_count[sorted_nums[-1]]=0
        
        
        print(smaller_count)
        result=[]
        for j in nums:
            result.append(smaller_count[j])
        return result