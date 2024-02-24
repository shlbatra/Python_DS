def smallestsubstringwithchars(input, match):
    dict_map={}
    for i in range(len(match)):
        dict_map[match[i]]=dict_map.get(match[i],0)+1
    print(dict_map)
    l=0
    min_substr=float('inf')
    min_substr_value=input
    for r in range(len(input)):
        # Check if available in dict and also make sure >0 to decrement as using sum below
        if str(input[r]) in dict_map:
            if dict_map[input[r]]>0:
                dict_map[input[r]]-=1
        if sum(dict_map.values()) == 0:
            while sum(dict_map.values()) == 0:
                min_substr=min(min_substr,r-l+1)
                if len(min_substr_value) > len(input[l:r+1]):
                    min_substr_value=input[l:r+1]
                if str(input[l]) in dict_map:
                    dict_map[input[l]]+=1                
                l=l+1
    return min_substr_value

input='xad9dk0293nc'
match='xd3'
print(input)
print(smallestsubstringwithchars(input, match))    
