# Find longest substring with k distinct chars (Window + Hashmap (char->int))
# Ex. [A, A, A, H, H, I, B, C]; 2 distint chars
# Leverage 2 pointer solution
class LongestSubstringKDistChars:
    
    def longest_substring_k_distinct_chars(self, arr, k):
        max_ws = -9999
        l = 0
        hm = {}
        for r in range(0, len(arr)):
            hm[arr[r]] = hm.get(arr[r], 0) + 1 # include in hashmap as window size increases
            
            while len(hm.keys()) > k: # If hashmap has more than k distinct chars
                hm[arr[l]] = hm[arr[l]] - 1 # shrink window size
                if hm[arr[l]] == 0:
                    del hm[arr[l]] # remove chars from hashmap if not exist in window
                l = l + 1
                
            max_ws = max(max_ws, r - l + 1) # calculate max window size
        
        return max_ws
        
arr = ['A','A', 'A', 'H', 'H', 'I', 'B', 'C']
k = 3
m = LongestSubstringKDistChars()
ans = m.longest_substring_k_distinct_chars(arr, k)
print(ans)