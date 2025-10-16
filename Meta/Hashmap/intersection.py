# Find elements that are part of both lists
# No duplicate elements in each list
# intersection([4,2,1,6], [3,6,9,2,10]) # -> [2,6]

def intersection(a, b):
    dict_map = {}
    intersect = []
    if len(a) <= len(b):
        for i, num in enumerate(a):
            dict_map[num] = dict_map.get(num, 0) + 1

        for num in b:
            if num in dict_map:
                intersect.append(num)
    else:
        for i, num in enumerate(b):
            dict_map[num] = dict_map.get(num, 0) + 1

        for num in a:
            if num in dict_map:
                intersect.append(num)

    return intersect

def intersection_set(a, b):
    set_a = set(a)
    intersect = []

    for num in b:
        if num in set_a:
            intersect.append(num)

    return intersect


ans = intersection([4,2,1,6], [3,6,9,2,10])
print(ans)

ans = intersection_set([4,2,1,6], [3,6,9,2,10])
print(ans)