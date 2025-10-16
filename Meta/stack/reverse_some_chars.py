# Input string and some chars
# function should return the string with the order of the given characters in reverse
# Ex. reverse_some_chars("computer", ["a", "e", "i", "o", "u"]) -> cemputor
# Stack - Last In First Out
# Use stack here to get reverse order as go last out first in
# Time complexity O(n+m)
# Space complexity O(n+m) -> stack + set for O(m) 

def reverse_some_chars(s, chars):
    char_set = set(chars)
    stack = []
    for ch in s:
        if ch in char_set: 
            stack.append(ch)

    ans = []

    for ch in s:
        if ch in char_set:
            ans.append(stack.pop())
        else:
            ans.append(ch)
    
    return ''.join(ans)

ans1 = reverse_some_chars("computer", ["a", "e", "i", "o", "u"])
print(ans1)
