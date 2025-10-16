# Fn accepts strings and return true / false if palindrome, string same both forward and backwards
# Ex. pop true, kakak true, boot false; kaak 
# l , r
# if l == r until l <= r then true else false
# Time O(n), Space O(1) - only use specific variables

def is_palindrome(s):
    
    if s == "": return True

    l, r = 0, len(s) - 1

    while l <= r:
        if s[l] != s[r]:
            return False
        l, r = l+1, r-1

    return True

ans1 = is_palindrome("kakak")
print(ans1)
ans2 = is_palindrome("kaak")
print(ans2)
ans3 = is_palindrome("     ")
print(ans3)
ans4 = is_palindrome("boot")
print(ans4)