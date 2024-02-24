## Given a sorted array of distinct integers and a target 
# value, return the index if the target is found. If not, 
# return the index where it would be if it were inserted
#  in order.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        Use Binary search, if found return mid 
        If not found, return start as the number will be inserted next to start number for it
        '''
        start=0
        end=len(nums)-1
        
        while start <= end:
            mid=int((start+end)/2)
            if nums[mid] > target:
                end = mid-1
            elif nums[mid] < target:
                start = mid+1
            else:
                return mid
        return start