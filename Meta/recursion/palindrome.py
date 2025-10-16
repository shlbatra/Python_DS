# Check if word is palindrome
# Check both ends and match and then confirm

def is_palindrome(s):
    # base case
    if len(s) == 0 or len(s) == 1: return True # Palindrome and stop from further recursion

    # recursive
    if s[0] == s[len(s)-1]:
        return is_palindrome(s[1:len(s)-1])

    return False # fallback base case to handle non palindrome

s = "kayak"
print(is_palindrome(s))

s = ""
print(is_palindrome(s))

s = "as"
print(is_palindrome(s))

s = "sahil"
print(is_palindrome(s))