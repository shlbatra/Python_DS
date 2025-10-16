# Pair product to get pair of values in list that product to target
# Ex. [3, 2, 5, 4, 1] tgt 8

def pair_product(numbers, target_product):
    num_dict = {}

    for i, num in enumerate(numbers):
        complement = target_product/num
        if complement in num_dict:
            return (num_dict[complement], i)
        num_dict[num] = i
    return None

ans = pair_product([3, 2, 5, 4, 1], 8)
print(ans)