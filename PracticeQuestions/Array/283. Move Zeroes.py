class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Instead of looking at this problem as moving 0s, think as moving non zero values
        2 points - prev and i 
        0,1,0,3,2   (prev=0,i=0)
        1,0,0,3,2   (prev=1,i=2)
        1,3,0,0,2   (prev=2,i=3)
        1,3,2,0,0   (prev=3,i=end of list)
        """
        prev=0
        for i in range(0,len(nums)):
            print(nums[i])
            if nums[i] != 0:
                temp = nums[i]
                nums[i] = nums[prev]
                nums[prev] = temp
                prev = prev+1
        return nums