def item_in_common1(list1, list2):
    common_elements = []
    for i in list1:
        for j in list2:
            if i == j:
                return True

    return False

def item_in_common2(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True
    for j in list2:
        if j in my_dict:
            return True
    return False


a = [1,3,5]
b = [2,4,6]

print(item_in_common2(a,b))
