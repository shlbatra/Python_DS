# Input list of numbers and a targetSum. 
# The function should return the number of subarrays that sum to the given target
# subarray is a consecutive series of one or more elements of the list
# Ex. subarray_sum_count([1, 3, 1, 4, -2, 3], 5) # -> 3
# subarray_sum_count([1, 3, 1, 4, 3], 5) # -> 2
# subarray_sum_count([1, 3, 1, 4, 3], 2) # -> 0

# get prefix sums
# for each prefix sum, count number of (tgt - a) = b

def subarray_sum_count(numbers, target_sum):
    # Time complexity O(n)
    # Space complexity O(n)
    #    1, 3, 1, 4, 3
    # 0, 1, 4, 5, 9, 12
    # tgt 5
    # 5-5, 9-5
    prefix_sum = [0]
    running_sum = 0

    for num in numbers:
        running_sum += num
        prefix_sum.append(running_sum)

    hm_seen = {}
    cnt = 0
    for ps in prefix_sum:
        complement = ps - target_sum
        
        if complement in hm_seen:
            cnt += hm_seen[complement]
        hm_seen[ps] = hm_seen.get(ps, 0) + 1

    return cnt

ans1 = subarray_sum_count([1, 3, 1, 4, -2, 3], 5)
print(ans1)
ans2 = subarray_sum_count([1, 3, 1, 4, 3], 5)
print(ans2)
ans3 = subarray_sum_count([1, 3, 1, 4, 3], 2)
print(ans3)