# sumOfLengths that takes in a list of strings and returns the total length of the strings.
# sum_of_lengths(['goat', 'cat', 'purple']) # -> 13
# sum_of_lengths([]) # -> 0
# empty return 0 - base case
# len(curr str) + pending strings
# Time O(n) - fn stack *O(n) - length = O(n*n)
# Space O(n) - fn stack*O(n) - new subarrays - length= O(n*n)

def sum_of_lengths(strings):
    if len(strings) == 0: return 0

    return len(strings[0]) + sum_of_lengths(strings[1:])

ans1 = sum_of_lengths(['bike', 'at', 'pencils', 'phone'])
print(ans1)

ans2 = sum_of_lengths([])
print(ans2)