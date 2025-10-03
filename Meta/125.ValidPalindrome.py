class Solution:

    def alphaNum(self, c):
            return (
                (ord('A') <= ord(c) <= ord('Z')) or
                (ord('a') <= ord(c) <= ord('z')) or
                (ord('0') <= ord(c) <= ord('9'))
            )

    def isPalindrome(self, s: str) -> bool:
        # Bad solution with extra memory
        # newS=""

        # for c in s:
        #     if c.isalnum():
        #         newS += c.lower()

        # return newS == newS[::-1]

        # Solution with 2 pointers

        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not self.alphaNum(s[left]):
                left += 1
            while right > left and not self.alphaNum(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
    
ans = Solution().isPalindrome("abcd 1221 dcba")
print(ans)  # Output: True