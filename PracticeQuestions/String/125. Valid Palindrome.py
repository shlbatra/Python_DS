class Solution:
    def isPalindrome_manual(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<r:
            while not self.alphaNum(s[l]) and l<r:
                l=l+1
            while not self.alphaNum(s[r]) and r>l:
                r=r-1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True
    
    def alphaNum(self,c):
            return (ord('A') <= ord(c) <= ord('Z') or 
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))


    def isPalindrome(self, s: str) -> bool:
        new_str=""
        for ch in s:
            if ch.isalnum():
                new_str = new_str + ch.lower()
        
        return (new_str==new_str[::-1])

s = Solution()
print(s.isPalindrome('aba'))