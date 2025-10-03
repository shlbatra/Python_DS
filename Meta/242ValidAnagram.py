class Solution:
    def isAnagram_sort(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
    def isAnagram_counter(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(s) # Counter automatically builds hashmap of freq of characters
    
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_map, t_map = {}, {}

        for i in range(len(s)):
            s_map[s[i]] = 1 + s_map.get(s[i], 0)
            t_map[t[i]] = 1 + t_map.get(t[i], 0)

        for ch in s_map:
            if s_map[ch] != t_map.get(ch, 0):
                return False
            
        return True
    
obj1 = Solution()
ans = obj1.isAnagram("anagram","nagaram")
print(ans)