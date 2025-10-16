#  The function should return a boolean indicating whether or not the string contains correctly matched brackets.
#  match brackets -> ( ) [ ] { }

# Use dict for (, [, {
# If open increment,
# close decrement
# if negative means close before open -> return False
# sum all 0 -> True else False
# O(n)
# dict -> O(6)

# Ex.
# befitting_brackets('(){}[](())') # -> True
# befitting_brackets('{[]}({}')
# befitting_brackets('') # -> True

def befitting_brackets(string):
    # This soln doesnt work if order of opening and closing paranthesis matters
    # Ex. False for ({)}
    b_map = {')': 0,'}': 0,']': 0}

    for ch in string:
        #print(ch)
        if ch == '(':
            b_map[')']+=1
        elif ch == '{':
            b_map['}']+=1
        elif ch == '[':
            b_map[']']+=1
        #print(b_map)
        if ch == ')':
            if b_map[')'] == 0: return False
            b_map[')'] -= 1
        if ch == '}':
            if b_map['}'] == 0: return False
            b_map['}'] -= 1
        if ch == ']':
            if b_map[']'] == 0: return False
            b_map[']'] -= 1
    ans = 0
    for val in b_map.values():
        ans = ans + val

    return ans == 0

def befitting_brackets_stack(string):
    # Right solution
    # ()[]
    # Stack -> (, () , [, [], empty
    # ([]}
    # Stack -> (,([, ([], (} - non empty
    # Time O(n) and Space O(n)
    stack = []
    d_map = {
        '(':')',
        '{':'}',
        '[':']'
        }

    for ch in string:
        # print(stack)
        if ch in d_map:
            stack.append(d_map[ch]) # append closing one to stack
        else:
            if stack and stack[-1] == ch: # stack has values and last popped value same as next char
                stack.pop() # matching found
            else:
                return False # if not found, return false
    return len(stack) == 0

ans1 = befitting_brackets_stack('(){}[](())')
print(ans1)
ans2 = befitting_brackets_stack('{[]}({}')
print(ans2)
ans3 = befitting_brackets('({)}')
print(ans3)

ans4 = befitting_brackets_stack('({)}')
print(ans4)