class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_lettercount={}
        dict_lettercount=collections.Counter(s)
        
        for i in range(len(s)):
            if dict_lettercount[s[i]] == 1:
                return i
        return -1
                
    def firstUniqChar_Alt(self, s: str) -> int:
        str_dict={}
        for ch in s:
            if ch not in str_dict:
                str_dict[ch] = True
            else:
                str_dict[ch] = False
        
        for i,ch in enumerate(s):
            if str_dict[ch]:
                return i
        return -1
            