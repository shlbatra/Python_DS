# Nesting score score based on following rules -

#[] is worth 1 point; [][][] -> 3 pts
#XY is worth X + Y points where X, Y are substrings of well-formed brackets
# Nested [[][][]] -> double pts -> 3*2 = 6
#[S] is worth S * 2 points where S is a substring of well-formed brackets
# Time complexity O(n) 
# Space O(n) - stack upto entire length


def nesting_score(string):
    # [[][]][]
    # 0 6 
    stack = [ 0 ] # empty string with score 0

    for ch in string:
        if ch == '[':
            stack.append(0) # keep adding
        elif ch == ']':
            num = stack.pop()
            if num == 0: # if 0, update to 1
                stack.append(1)
            else:
                while stack[-1] != 0: # if 1 then continue summing till get to last 0
                    num = num + stack.pop()
                stack.append(num*2)
    
    return sum(stack)

def nesting_score_alt(string):
    stack = [0]
  
    for char in string:
        if char == '[':
            stack.append(0)
        else:
            popped = stack.pop() # checking popped to either update with 1 or numtiply by 2
            if popped == 0:
                stack[-1] += 1 # update last element by 1 
            else:
                stack[-1] += 2 * popped # update last element 
        #print(stack)

    return stack[0]

ans1 = nesting_score_alt('[[][]][]')
print(ans1)
ans1 = nesting_score_alt('[[][][]][[]]')
print(ans1)