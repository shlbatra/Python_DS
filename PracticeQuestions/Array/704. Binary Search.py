# Given an array of integers nums which is sorted in 
# ascending order, and an integer target, write a function 
# to search target in nums. If target exists, then return
#  its index. Otherwise, return -1.

# Get O(LogN) solution

class Solution:
    def search(self, nums: List[int], target: int) -> int:
            '''
            Make sure you do start <= end and return -1 after the loop completes for something not found
            '''
            start = 0
            end = len(nums)-1
            
            while start <= end:
                mid = int((start + end)/2)
                num = nums[mid]
                if num==target:
                    return mid
                elif num<target:
                    start = mid+1
                elif num>target:
                    end = mid-1
            return -1