# Generate items in eithers lists but not in both lists (Union)
# No duplicate elements
# exclusive_items([4,2,1,6], [3,6,9,2,10]) # -> [4,1,3,9,10]


def exclusive_items(a, b):
    a_set = set(a) # Runs linear time, O(n)
    b_set = set(b)
    res = []
    for item in b:
        if item not in a_set:
            res.append(item)

    for item in a:
        if item not in b_set:
            res.append(item)

    return res

ans = exclusive_items([4,2,1,6], [3,6,9,2,10])
print(ans)