class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        '''
        Include 10 digit sequence in hash set and then check against it 
        Add matches to hash set to keep it unique 
        
        Optimization -> 4 diff chars -> 8 bits. Map chars to 00,01,10,11 so need 2 bits
        10 characters with 2 bits -> 20 bits in each substring then fit in 32 bit integer
        Time complexity - Same , HashSet 32 bit mapping 
        '''
        
        seen,res = set(), set()
        
        for l in range(len(s)-9):
            cur = s[l:l+10]
            if cur in seen:
                res.add(cur)
            seen.add(cur) #Ignore as duplicate else would require else case here
        return list(res)