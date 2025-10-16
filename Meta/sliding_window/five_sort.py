#  The function should rearrange elements of the list such that all 5s appear at the end.
# Your function should perform this operation in-place by mutating the original list. 
# Ex. [5, 0] -> [0, 5]
# [5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5] ->  [4, 1, 2, 1, 2, 3, 5, 5, 5, 5, 5, 5, 5, 5] 

# Iterate through list with left and right
# As see 5, reirange with current iteration 
# 5, 0, 5, 1, 2 # 0, 4
# 2, 0, 5, 1, 5 # 1, 3
# 2, 0, 5, 1, 5 # 2, 3
# 2, 0, 1, 5, 5 # 3, 2 -> end loop

# Space O(1) - update same
# Time O(n)

def five_sort(nums):
    l, r = 0, len(nums) -1

    while l <= r:
        # print(l, r)
        if nums[r] == 5:
            r = r - 1
        elif nums[l] != 5:
            l = l + 1
        elif nums[l] == 5:
            nums[l] = nums[r]
            nums[r] = 5
            l = l + 1
            r = r - 1
    return nums

ans1 = five_sort([5, 0])
print(ans1)
ans1 = five_sort([5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5])
print(ans1)
ans3 = five_sort([1, 2, 5, 3, 5, 5, 5])
print(ans3)