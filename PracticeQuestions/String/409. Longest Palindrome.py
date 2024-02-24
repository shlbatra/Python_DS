#Given a string s which consists of lowercase or uppercase 
# letters, return the length of the longest palindrome that 
# can be built with those letters.
# Alternate way - char_count=collections.Counter(s)

class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count={}
        for char in s:
            char_count[char] = char_count.get(char,0) + 1
        
        odd_present=0
        final_count=0
        for char in char_count:
            if char_count[char]%2 == 0:
                final_count = final_count + char_count[char]
            else:
                final_count = final_count + (char_count[char]-1)
                odd_present=1
                
        return(final_count+odd_present)
