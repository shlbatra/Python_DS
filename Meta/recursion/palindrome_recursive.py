# takes in string and returns returns a boolean indicating whether or not the string is the same forwards and backwards.

# Base case empty return true
# Base case left with singale character return true
# Base case if first and last not same return false
# continue first + 1 and last - 1
# Time -> O(n) call stack * O(n) -> slice -> O(n*n)
# Space -> O(n) call stack * O(n) -> slice -> O(n*n)


def palindrome(s):
    if len(s)<=1: return True
    if s[0] != s[len(s)-1]: return False
    return palindrome(s[1:len(s)-1]) # palindrome(s[1:-1])

ans1 = palindrome("pop")
print(ans1)

ans2 = palindrome("pops")
print(ans2)

ans3 = palindrome("")
print(ans3)

ans4 = palindrome("ab")
print(ans4)

ans5 = palindrome("a")
print(ans5)