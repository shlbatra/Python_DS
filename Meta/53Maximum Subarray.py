from typing import List

class Solution:

    def maxSubArray_Optimized(self, nums: List[int]) -> int:
        maxSub = nums[0] # start with something and not 0 as negative values in example
        currSum = 0
        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum = currSum + n
            maxSub = max(maxSub, currSum)
        return maxSub

    def maxSubArray(self, nums: List[int]) -> int:
        # Ex input -2, 1, -3, 4, -1, 2, 1, -5, 4
        # start -2 and Add 1 -> -1 not contribute so ignore -2
        # 1 and add -3 get -2 not contribute 
        # then next 4 -> -2 not help so drop before
        # then next -1 get 3 continue
        # then next 2 get 5 continue
        # then next 1 get 6 continue (Max)
        # then next -5 get 1 continue as positive
        # then next 4 get 5 continue and end
        maxSub = nums[0] # start with something and not 0 as negative values in example
        l, r = 0, 1
        subarrSum = 0
        while r < len(nums):
            if subarrSum < 0:
                subarrSum = 0
                l = l+1
            subarrSum = subarrSum + nums[r]
            # print(f"{subarrSum}")
            maxSub = max(maxSub, subarrSum)
            r = r + 1
        return maxSub

obj1 = Solution()
ans = obj1.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(ans)