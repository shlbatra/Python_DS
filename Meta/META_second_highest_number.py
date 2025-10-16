# Find second highest number 
# Ex. 12345 -> 54312
# 900 -> 090
# 111 -> No second highest number
# 1221 -> 2121

def second_highest(numbers):

    if len(set(numbers)) == 1: return -1

    sorted_numbers = sorted(numbers, reverse = True)

    idx = 0

    for i in range(0, len(sorted_numbers)-1):
            # 5, 4, 3, 2, 1 -> idx = 0
            # 2, 2, 1, 1 -> idx = 2
            # 2, 2, 1
            if sorted_numbers[i] != sorted_numbers[i+1]:
                idx = i

    tmp = sorted_numbers[idx]
    sorted_numbers[idx] = sorted_numbers[idx+1]
    sorted_numbers[idx+1] = tmp

    return sorted_numbers

ans1 = second_highest([1, 2, 3, 4, 5])
print(ans1)
ans2 = second_highest([9, 0, 0])
print(ans2)
ans3 = second_highest([1, 1, 1])
print(ans3)
ans4 = second_highest([1, 2, 2, 1])
print(ans4)


    





