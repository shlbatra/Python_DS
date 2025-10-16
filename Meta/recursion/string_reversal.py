# Reverse input string
# Ex. the -> eht

def string_reverse(s):
    # Base case -> return if empty string
    if s == "": return ""
    # recursive code -> keep moving to next character in string
    return string_reverse(s[1:]) + s[0] # Stack last in first out
    #      Shrink problem space + Minimum amt of work

s = "sahil batra"
print(string_reverse(s))