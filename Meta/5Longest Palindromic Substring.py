class Solution:
    def longestPalindrone(self, s: str) -> str:
        # Input babad
        # Output bab / aba
        # Check for b -> expand only 1
        # Check for a -> expand 3 - also include edge case for even length as calculating odd length palindrome only
        # Input cbbd
        # Outut bb
        # When expand from b, right one is b
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length palindromes
            l, r = i, i
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    resLen = r-l+1
                    res = s[l:r+1]
                l, r = l-1, r+1
            # even length palindromes; bbbb
            l, r = i, i+1
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    resLen = r-l+1
                    res = s[l:r+1]
                l, r = l-1, r+1

        return res, resLen

obj1 = Solution()
ansstr, ans = obj1.longestPalindrone("babad")
print(f"{ansstr} and {ans}")

obj2 = Solution()
ansstr, ans = obj2.longestPalindrone("cbbd")
print(f"{ansstr} and {ans}")