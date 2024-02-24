# Given a non-empty array of integers nums, every element 
# appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime 
# complexity and use only constant extra space.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        acc = 0
        for num in nums:
            acc = acc^num
            print(f"num is {num} and acc is {acc}")
        return acc

    def singleNumber1(self, nums: List[int]) -> int:
        nums_dict = collections.Counter(nums)
        for i,j in nums_dict.items():
            if j != 2:
                return i
        print(nums_dict)