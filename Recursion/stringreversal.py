def stringreversal(s):
    if s == "":
        return ""
    return stringreversal(s[1:len(s)]) + s[0]

input = 'sahil batra'
print(input)
ans = stringreversal(input)
print(ans)
