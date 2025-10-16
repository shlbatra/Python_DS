# Return list with elements in both lists. For repeated items, get the same number of times as in both list
# ["q", "b", "m", "s", "s", "s"]; ["s", "m", "s"] -> ["s", "m", "s"]
# Time O(n+m)
# Space O(n)

def intersection_with_dupes(a, b):
    h_map = {}
    res = []
    for element in a:
        h_map[element] = h_map.get(element, 0) + 1

    for element in b:
        if element in h_map and h_map[element] > 0:
            h_map[element] -= 1
            res.append(element)

    return res

def intersection_with_dupes_alt(a, b):
    h_map_a = {}
    h_map_b = {}
    res = []
    for element in a:
        h_map_a[element] = h_map_a.get(element, 0) + 1
    for element in b:
        h_map_b[element] = h_map_b.get(element, 0) + 1

    for key_a in h_map_a.keys():
        for i in range(0, min(h_map_a.get(key_a,0), h_map_b.get(key_a,0))):
            res.append(key_a)

    return res

ans1 = intersection_with_dupes_alt(["q", "b", "m", "s", "s", "s"], ["s", "m", "s"] )
print(ans1)

a = []
b = [] 
for i in range(0, 15):
  a.append(i)
  b.append(i)

ans2 = intersection_with_dupes(a, b)
print(ans2)