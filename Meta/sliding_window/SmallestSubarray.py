# Find smallest subarray that has sum greater than target
# Ex. [4, 2, 2, 7, 8, 1, 2, 8, 10]; target 8
# Leverage 2 pointer solution
class SmallestSubArrayTgt:
    
    def smallest_subarray_tgt(self, arr, tgt):
        run_sum = 0
        smallest = 9999
        l = 0
        for r in range(0, len(arr)):
            run_sum += arr[r]
            
            while run_sum >= tgt:
                smallest = min(smallest, (r-l+1)) # get window size
                run_sum -= arr[l] # remove left most element
                l = l+1 # increment until run sum greater than target
                
                
        return smallest

arr = [4, 2, 2, 7, 8, 1, 2, 8, 10]
tgt = 20

m = SmallestSubArrayTgt()
ans = m.smallest_subarray_tgt(arr, tgt)
print(ans)