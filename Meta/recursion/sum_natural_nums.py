# Input 10
# Return 1+2+3+4+5+6+7+8+9+10


def sum_natural_nums(num):
    if num == 0: return 0

    return num + sum_natural_nums(num-1)


print(sum_natural_nums(10))