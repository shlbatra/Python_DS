# Pair sum to get pair of values in list that sum to target
# Ex. [3, 2, 5, 4, 1] tgt 8

def sum_pair(arr, tgt):
    num_dict = {} # Store as num, index 

    for i, num in enumerate(arr):
        complement = tgt - num
        if complement in num_dict:
            return (num_dict[complement], i)
        num_dict[num] = i
    return None

ans = sum_pair([3, 2, 5, 4, 1], 8)
print(ans)

ans = sum_pair([9, 2, 11, -4, 1], 7)
print(ans)