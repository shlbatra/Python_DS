# Retrun boolean to indicate whether or not list contains unique items
# ["q", "r", "s", "a"] -> True
# ["q", "r", "s", "a", "r", "z"] -> False

# Create set
# see if element in set then false else true
# O(n) both space and time complexity

def all_unique(items):
    items_set = set()

    for item in items:
        if item in items_set:
            return False
        items_set.add(item)

    return True

ans1 = all_unique(["q", "r", "s", "a"])
print(ans1)

ans2 = all_unique(["q", "r", "s", "a", "r", "z"])
print(ans2)