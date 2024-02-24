class Solution:

    def reverseString_twopointer(self, s: List[str]) -> None:
        """
        Get first and last pointer and swap first and last till we get to the middle of the string
        """
        first=0
        last=len(s)-1
        while first<last:
            temp=s[first]
            s[first]=s[last]
            s[last]=temp
            first+=1
            last-=1
        return s
    def reverseString_alternate(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        Similar logic to two pointer above but using some python magic
        """

        for i in range(len(s)//2): 
            s[i], s[-i-1] = s[-i-1], s[i]   
        return s
        