# reverse_string, that takes in a string as an argument. The function should return the string with its characters in reverse order
# do recursively
# reverse_string("hello") # -> "olleh"
# if empty return base case
# else return  reverse_string(pending string) + curr character
# Time complexity = O(n) stack * O(n) sub array
# Space complexity = O(n) stack * O(n) sub array

def reverse_string(s):
    if s == "": return ""

    return "".join(reverse_string(s[1:]) + s[0])


ans1 = reverse_string("hello")
print(ans1)

ans2 = reverse_string("")
print(ans2)

ans3 = reverse_string("stopwatch") 
print(ans3)