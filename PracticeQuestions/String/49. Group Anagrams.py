class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            
        dict_map=defaultdict(list) #map charCount to list of Anagrams
        
        for word in strs:
            arr = [0]*26
            for letter in word:
                arr[ord(letter)-ord('a')]+=1
            dict_map[tuple(arr)].append(word)
        return dict_map.values()



    def groupAnagrams_sorted(self, strs: List[str]) -> List[List[str]]:
        
        ans = collections.defaultdict(list)
        print(ans.items())
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return(ans.values())