class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        Create two dict maps for s1 and window of s2 
        Compare the two dictionaries and return true if a match else return false 
        O(n)+O(26.n)
        '''
        if len(s1) > len(s2):return False
        dict_map_s1={}
        for i in range(len(s1)):
           dict_map_s1[s1[i]]=dict_map_s1.get(s1[i],0)+1
        window_size=len(s1)
        print(window_size)
        l,r=0,0
        for r in range(len(s2)):
            while (r-l < window_size-1):
                r=r+1
            if len(s2[l:r+1]) == window_size:
                dict_map_s2={}
                temp=s2[l:r+1]
                print(temp)
                for i in range(len(temp)):
                    dict_map_s2[temp[i]]=dict_map_s2.get(temp[i],0)+1
                if dict_map_s1 == dict_map_s2:
                    return True
                l=l+1
        return False

    def checkInclusion_bettersoln(self, s1: str, s2: str) -> bool:

            '''
            Create two arrays for s1 and window of s2 
            Compare the two arrays and get sum of matches. If match, then 26 
            As you run through window, check if new char updates s2index in such a way that matches number go up 
            O(n)
            '''
            if len(s1) > len(s2):return False
            
            s1Count,s2Count=[0]*26,[0]*26
            
            for i in range(len(s1)):
                s1Count[ord(s1[i])-ord('a')]+=1
                s2Count[ord(s2[i])-ord('a')]+=1
            matches=0
            for i in range(26):
                matches+= (1 if s1Count[i]==s2Count[i] else 0)
            l=0
            for r in range(len(s1),len(s2)):
                if matches == 26:
                    return True
                index = ord(s2[r]) - ord('a')  #Add character from right 
                s2Count[index]+=1
                if s1Count[index] == s2Count[index]: #if match then matches increment by 1
                    matches+=1
                elif s1Count[index]+1 == s2Count[index]:  #if not match then matches decrement by 1
                    matches-=1
                
                index = ord(s2[l]) - ord('a') #Remove character from left
                s2Count[index]-=1
                if s1Count[index] == s2Count[index]: #if match then matches increment by 1
                    matches+=1
                elif s1Count[index]-1 == s2Count[index]: #if already match removed then matches decrement by 1
                    matches-=1
                l+=1
                    
            return matches == 26  #Check for the last iteration on loop as well