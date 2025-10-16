# Compress where consecutive occurrences of the same characters are compressed into the number of occurrences 
# followed by the character. Single character occurrences should not be changed
# ex. 'aaa' -> 3a, 'a' -> a
# 'nnneeeeeezz' -> 3n6e2z

# 2 ptrs
# Keep moving ptr till diff character
# Count as num
# then append with char ( if != 1)
# return array joined
# Time O(n) -> string length
# Space O(n) -> as create output string -> concatenate to strin
def compress(s):
    s = s + '!' # to take into acct last group to fix out of bounds error ( consider diff character)
    i, j = 0, 0
    res = []

    while j <= len(s) -1 :
        if s[i] == s[j]: # progress j till diff.
            j = j + 1
            #print(j, i)
        else:
            #print(j, i)
            # j = 3, i = 3
            if (j-i) > 1:
                res.append(str(j-i))
            res.append(s[i])
            i = j
            # j =3, i =3
            
    return ''.join(res)

ans1 = compress('nnneeeeeezz')
print(ans1)
ans2 = compress('nnn')
print(ans2)
ans3 = compress('n')
print(ans3)