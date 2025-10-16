# sort elements of a list using merge sort
# Ex. [10, 4, 42, 5, 8, 100, 5, 6, 12, 40] -> [ 4, 5, 5, 6, 8, 10, 12, 40, 42, 100 ] 
# Divide and Conquer algo
# Recursion and break down 
# Final combine in a merge function for all broken down sort algos -> merge two sorted arrays - Time O(a+b)
# Log repeated division logn -> as keep dividing array by 2 on each step
# Time complexity O(nlogn)


def merge_sort(nums):
    if len(nums) <= 1: return nums # simple case of small list

    mid = len(nums) // 2 
    left_sorted = merge_sort(nums[:mid])
    right_sorted = merge_sort(nums[mid:])

    return merge(left_sorted, right_sorted)

def merge(left, right):
    # take 2 sorted arrays and return sorted array

    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i = i + 1
        else:
            merged.append(right[j])
            j = j + 1

    while i < len(left):
        merged.append(left[i])
        i = i + 1

    while j < len(right):
        merged.append(right[j])
        j = j + 1

    return merged

ans = merge_sort([10, 4, 42, 5, 8, 100, 5, 6, 12, 40])
print(ans)