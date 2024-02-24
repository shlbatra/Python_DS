class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        [1,2,3,4,5] - rotate by 2  ..Final Output [4,5,1,2,3]
        first reverse 5,4,3,2,1   -> 5,4 revese to 4,5    and 3,2,1 reverse to 1,2,3
        Concatenate both -> 4,5,1,2,3
        """
        n=len(nums)
        k=k%n
        nums[:]=nums[::-1]
        nums[:]=nums[:k][::-1]+nums[k:n][::-1]

    def rotate_extramemory(self, nums: List[int], k: int) -> None:
        """
        Go through list and update based on moving the new array by (i+k)%n
        """
        res=[0]*len(nums)
        for i in range(len(nums)):
            res[(i+k)%len(nums)]=nums[i]
        print(res)
        nums[:]=res