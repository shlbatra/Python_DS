# For two strings, verify boolean if string1 subsequence of string2
# Subsequence is a string that can be formed by deleting 0 or more characters from another string
# Ex/. is_subsequence("bde", "abcdef") # -> True
# is_subsequence("bda", "abcdef") # -> False
# is_subsequence("riverbed", "river") # -> False
# is_subsequence("river", "riverbed") # -> True

# Approach - wont work as cannot rearrange -> only delete from string1 to get string2
# hash map for string 2
# if find everything in string 1, return true
# Time O(n+m); n - string1, m - string2
# Space O(n)

# Approach that works
# s1 and s2 -> 2 ptrs
# for s1 ptr, if s2 ptr same continue
# for s1 ptr, if s2 ptr diff -> go to next until end of string, if end of string return
# Time O(n) - longer sequence length
# Space -> O(1)

def is_subsequence(string_1, string_2):
    i1, i2 = 0, 0
    # string_1 sub string of string_2
    while i1 < len(string_1) and i2 < len(string_2):
        if string_1[i1] != string_2[i2]:
            i2 = i2+1
        elif string_1[i1] == string_2[i2]:
            i1 = i1+1
            i2 = i2+1
        
    if i1 == len(string_1):
        return True
    else:
        return False
    
ans1 = is_subsequence("bde", "abcdef")
print(ans1)
ans2 = is_subsequence("bda", "abcdef")
print(ans2)
ans3 = is_subsequence("river", "riverbed")
print(ans3)
ans4 = is_subsequence("riverbed", "river")
print(ans4)