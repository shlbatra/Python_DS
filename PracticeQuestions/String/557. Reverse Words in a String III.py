class Solution:
    def reverseWords(self, s: str) -> str:
            '''
            Till we not get ' ', keep appending every letter in word as reverse in rev_str
            Once we get to ' ', then add the reversed word to final result. Do the same for last word as well
            as part of return statement
            '''
            res=''
            rev_str=''
            for i in range(len(s)):
                if s[i]==' ':
                    print(rev_str)
                    res=res+rev_str+" "
                    rev_str=''
                else:
                    rev_str=s[i]+rev_str
            return res+rev_str

    def reverseWords_faster(self, s: str) -> str:

            '''
            Use python functionality to split the sentence
            Once done, reverse word and append it back to result
            '''
            res=""
            for word in s.split(' '):
                word=word[::-1]
                res=res+word+" "
            return res[:-1]

    def reverseWords(self, s: str) -> str:
            '''
            Single line solution similar to faster solution above
            '''
            return ' '.join(word[::-1] for word in s.split(' '))