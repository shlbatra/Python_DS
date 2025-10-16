# Fn check if string has well formed paranthesis. Ex. start ( then end with )
# paired_parentheses("(david)((abby))") # -> True
# () -> if contain -> add to stack > ()(())
# Mantain count for opening paranthesis and then reduce to 0 as see closing paranthesis; if -ve then closing before opening - not possible
# O(n+p) -> paranthesis
# Space O(1)

def paired_parentheses(string):
    # Build O(n) solution
    p_set = set(["(",")"])
    temp = []
    for ch in string:
        if ch in p_set:
            temp.append(ch)

    cnt = 0
    # print(temp)
    for ch in temp:
        if ch == "(":
            cnt+=1
        else:
            cnt-= 1
        if cnt < 0: return False # If closing paranthesis extra before opening paranthesis

    if cnt == 0:
        return True
    else:
        return False

def paired_parentheses_alt(string):
    cnt = 0

    for ch in string:
        if ch == '(':
            cnt += 1
        if ch == ')':
            if cnt == 0:
                return False # If closing paranthesis extra before opening paranthesis
            cnt -= 1

    if cnt == 0:
        return True
    else: return False
             

ans1 = paired_parentheses("(david)((abby))")
print(ans1)
ans2 = paired_parentheses("(())(water()()")
print(ans2)
ans3 = paired_parentheses("")
print(ans3)