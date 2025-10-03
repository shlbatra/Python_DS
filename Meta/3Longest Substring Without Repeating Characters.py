class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Ex. abcabcbb
        # Ans 3
        # Start a and continue to b and c -> keep adding to set (Window 3)
        # Once next a comes available in set so move left ptr to b (Window 3)
        # Once next b comes available in set so move left ptr to c (Window 3)
        # once next c comes available in set so move left ptr to b (Window 2)
        # Last b - window of 1 only
        charSet = set()

        l = 0
        l_substr = 0
        for r in range(len(s)):
            while s[r] in charSet: # Until we have duplicates
                charSet.remove(s[l]) # remove all characters till we have duplicate
                l = l + 1    # keep updating window on left end
            charSet.add(s[r]) # add right most new characters
            l_substr = max((r-l+1), l_substr) # Keep updating max window
            r = r + 1
        
        return l_substr
        
obj1 = Solution()
ans = obj1.lengthOfLongestSubstring("abcabcbb")
print(ans)