class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        
        for i in range(len(s)):
            #Odd Palindromes
            l,r=i,i
            count=count+self.countPali(s,l,r)
            
            #Even Palindromes
            l,r=i,i+1
            count=count+self.countPali(s,l,r)
        return count
    
    def countPali(self,s,l,r):
        c=0
        while l>=0 and r<len(s) and s[l]==s[r]:
                c+=1
                l=l-1
                r=r+1
        return c