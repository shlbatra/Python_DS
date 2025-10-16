# Fn take compressed string and return decompressed string
# The compression format of the input string is 'n{sub_string}', where the sub_string within braces should be repeated n times
# n between 1 and 9
# decompress_braces("2{q}3{tu}v") -> qqtututuv
# decompress_braces("2{3{r4{e}r}io}") -> reeeerreeeerreeeerioreeeerreeeerreeeerio

# Keep adding to stack numbers and chars 
# When opposite bracket comes
# get last number and chars

# 2{q}3{tu}v
# Stack -> q, q, tututu, v
# 2{3{r4{e}r}io}
# Stack -> reeeerreeeerreeeerioreeeerreeeerreeeerio
# Time o(9^m*s) -> m grps and s chars
# Space o(9^m*s)

def decompress_braces(string):
    stack = []
    chars = []

    num_set = set([0,1,2,3,4,5,6,7,8,9])
    for ch in string:
        if ch in num_set:
            stack.append(ch) # keep adding nums 
        else:
            if ch == '}': # special logic to get segment and nums when } arrives
                segment = ''
                while stack[-1].isalpha():
                    segment = stack.pop() + segment  # create segment making sure last element on right. ex 'er'
                num = stack.pop() # get num
                # print(segment, num)
                # print(str(segment) * int(num))
                stack.append(str(segment) * int(num)) # add back to stack
            elif ch != '{': # keep adding chars and exclude {
                stack.append(ch)
        # print(ch, stack)
    return ''.join(stack)

ans1 = decompress_braces("2{q}3{tu}v")
print(ans1)
ans2 = decompress_braces("2{3{r4{e}r}io}")
print(ans2)