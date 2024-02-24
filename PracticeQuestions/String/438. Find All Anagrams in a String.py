class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        Input: s = "cbaebabacd", p = "abc"
        Output: [0,6]
        We create two hash maps for s & p to match (Pick substring of s matching p)
        Do intial hash map match
        Then run sliding window starting l from len(p) and ending len(s)
        As iterate, remove s[l] & add s[r] from hashmap for s 
        and match s & p dictionaries and append to res - l. 
        Pop any l element that goes to 0 from s dictionary
        '''
        if len(p) > len(s):
            return []
        dict_words_s = {}
        dict_words_p = {}
        
        for i in range(len(p)):
            dict_words_p[p[i]]=dict_words_p.get(p[i],0)+1
            dict_words_s[s[i]]=dict_words_s.get(s[i],0)+1
        
        res=[0] if dict_words_s==dict_words_p else []
        l=0
        for r in range(len(p),len(s)):
            dict_words_s[s[r]] = dict_words_s.get(s[r],0) + 1
            dict_words_s[s[l]] = dict_words_s[s[l]] - 1        
            if dict_words_s[s[l]] == 0:
                dict_words_s.pop(s[l])
            l=l+1
            
            if dict_words_s==dict_words_p:
                res.append(l)
            
        return res