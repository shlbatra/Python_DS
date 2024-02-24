class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Using Sliding Window Technique
        Both l and r start with 0 and we keep a set with letters already seen
        Continue moving right by adding letter to set. If letter is seen, then increment left and remove left char
        Final answer is max sequence of (r-l+1)
        '''
        set_letter=set()
        final=0
        l=0
        r=0
        for r in range(len(s)):
            while s[r] in set_letter:
                set_letter.remove(s[l])
                l=l+1
            set_letter.add(s[r])
            final = max(final,r-l+1)
        return final