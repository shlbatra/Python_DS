# Uncompress with format provided as 
# "2c3a1t" -> ccaaat
# "20c3a1t" -> problem 
# <num><char>
# time O(n*m) # n - num of grps, m - max num found in any group 
# Space O(n*m)

def uncompress(s):
    num, ch = 0, 0
    res = []
    while ch <= len(s) - 1:

        while not s[ch].isalpha():
            ch += 1 
        num_grp = s[num:ch]
        print(num_grp)
        for i in range(0, int(num_grp)):
            res.append(s[ch])
        #print(res)
        ch = ch + 1
        num = ch
        
    return ''.join(res)


def uncompress_alt(s):
    numbers = '0123456789'
    num, ch = 0, 0
    res = []
    while ch <= len(s) - 1:
        # 200c
        while s[ch] in numbers:
            ch += 1 
        num_grp = s[num:ch]
        #print(num_grp)
        # alternate res.append(s[ch] * num_grp)
        for i in range(0, int(num_grp)):
            res.append(s[ch])
        #print(res)
        ch = ch + 1
        num = ch
        
    return ''.join(res)

ans1 = uncompress("2x127y")
print(ans1)
ans2 = uncompress("20c3a1t")
print(ans2)
ans1 = uncompress_alt("2x127y")
print(ans1)
ans2 = uncompress_alt("20c3a1t")
print(ans2)