# Get running sum at each element of list as new list
# Ex. result[i] = numbers[0] + numbers[1] + numbers[2] + ... + numbers[i]
# running_sum([4, 2, 1, 6, 3, 6]) # -> [ 4, 6, 7, 13, 16, 22 ] 
# running_sum([]) # -> [ ] 
# running_sum([2]) # -> [ 2 ]
# Approach
#  For each num, keep sum and then append to new res
# return res
# For empty, just return empty
# Time O(n)
# Space O(n)


def running_sum(numbers):
    res = []
    running_sum = 0
    for num in numbers:
        running_sum += num
        res.append(running_sum)

    return res

ans1 = running_sum([4, 2, 1, 6, 3, 6])
print(ans1)
ans2 = running_sum([2])
print(ans2)
ans2 = running_sum([])
print(ans2)