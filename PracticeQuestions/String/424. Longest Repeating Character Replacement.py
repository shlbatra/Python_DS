class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Combine hash map and sliding window algo
        Keep hash map for count of diff chars in window and get 
        the most frequent char. So Len of Window - Max Freq Value < = k 
        If, > k, then move left ptr and remove left character from dict 
        and continue. Calculate your final length of substring
        '''
        count = {}
        l=0
        res=0
        for r in range(len(s)):
            count[s[r]]=1+count.get(s[r],0)
            while (r-l+1) - max(count.values()) > k:
                count[s[l]]-=1
                l = l + 1
            res = max(res,(r-l+1))    
        return res