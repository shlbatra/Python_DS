#  list of numbers and a target_sum - return a boolean indicating whether or not there exists 
#  a subarray of numbers that sums to the given target.
# subarray is a consecutive series of one or more elements of the list.

# has_subarray_sum([1, 3, 1, 4, 3], 8) # -> True
# has_subarray_sum([1, 1, 1, 1, 1, 1, 1, 1, 1], 10) # -> False

# Start l and l+1
# Keep including next till sum < tgt
# if sum > tgt then move left one 
# Time O(n)
# Space O(1)

def has_subarray_sum_positive_numbers(numbers, target_sum):
    # Makes assumption that window sum can decrease with negative numbers
    i, j = 0, 1
    running_sum = numbers[i]

    if running_sum == target_sum: return True # For single element

    while j <= len(numbers) - 1:

        if running_sum == target_sum:
            return True
        elif running_sum < target_sum:
            running_sum += numbers[j]
            j = j + 1
        elif running_sum > target_sum:
            running_sum -= numbers[i]
            i = i + 1 

    return False

def has_subarray_sum_brute_force(numbers, target_sum):
    # Time complexity O(n3) -> loop for start and end, and then n -> loop add all elements between start and end
    # Ex. #   1, 3, 1, 4, 3
    for start in range(0, len(numbers)):
        for end in range(start+1, len(numbers)+1):
            curr_sum = 0
            for i in range(start, end):
                curr_sum = curr_sum + numbers[i]
            if curr_sum == target_sum:
                return True

    return False

def has_subarray_sum_prefix_sum(numbers, target_sum):
    # Get running sum till the element
    # Use prefix sum to get sum of any sub array -> 
    #   1, 3, 1, 4, 3
    #0, 1, 4, 5, 9, 12 
    #Time O(n2) -> calculate prefix + iterate through prefix as n2
    prefix_sum = [0]
    running_sum = 0
    for num in numbers:
        running_sum += num
        prefix_sum.append(running_sum)

    for start in range(0, len(prefix_sum)):
        for end in range(start+1, len(prefix_sum)):
            if (prefix_sum[end] - prefix_sum[start]) == target_sum:
                return True

    return False


def has_subarray_sum_set(numbers, target_sum):
    # prefix sum
    # find two numbers diff = tgt (Pair sum)
    # Time complexity O(n) -> prefix sum + iterate over prefix sum
    # Space complexity - O(n+n) - prefix sum + set 
    #   1, 3, 1, 4, 3
    #0, 1, 4, 5, 9, 12 
    # Tgt 8 
    # ex. b - a = tgt OR b-tgt = a
    prefix_sum = [0]
    running_sum = 0
    for num in numbers:
        running_sum += num
        prefix_sum.append(running_sum)
    p_set = set()
    for num in prefix_sum:
        if (num-target_sum) in p_set:
            return True
        p_set.add(num)
    return False


ans1 = has_subarray_sum_set([1, 3, 1, 4, 3], 8)
print(ans1)
ans2 = has_subarray_sum_set([1, 1, 1, 1, 1, 1, 1, 1, 1], 10)
print(ans2)
ans3 = has_subarray_sum_set([5], 5)
print(ans3)
ans4 = has_subarray_sum_set([4, 2, 5, 1, 5, -2, 8], 9)
print(ans4)