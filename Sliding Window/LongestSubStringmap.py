# Longest Substring Length with K distinct characters

def smallestsum_subarray(inputstring,k):
    dict_map={}
    l=0
    max_substring=float('-inf')

    for r in range(0,len(inputstring)):
        dict_map[inputstring[r]]=dict_map.get(inputstring[r],0) + 1
        while len(dict_map) > k:
            dict_map[inputstring[l]]-=1
            if dict_map[inputstring[l]] == 0:
                del dict_map[inputstring[l]]
            l=l+1
        max_substring=max(max_substring,r-l+1)
    return max_substring

inputstring='aaaaahhibhc'
k=2
print(smallestsum_subarray(inputstring,k))