class Solution:
    def isValid(self, s: str) -> bool:
        dict_map={
                '(':')', 
                '{':'}', 
                '[':']', 
                 }
        result=0
        stack=[]
        
        if len(s)<=1:
            return False
        
        for i in range(len(s)):
            if s[i] in dict_map.keys():
                stack.append(s[i])
            
            if s[i] in dict_map.values():
                if len(stack) == 0:
                    return False
                val = stack.pop()
                if dict_map[val]!=s[i]:
                    return False
        if len(stack)>0:
            return False
        return True