def merge(list1,list2):
    i = 0
    j = 0
    merge_list = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merge_list.append(list1[i])
            i = i + 1
        else:
            merge_list.append(list2[j])
            j = j + 1
    while i < len(list1):
        merge_list.append(list1[i])
        i = i + 1
    while j < len(list2):
        merge_list.append(list2[j])
        j = j + 1
    return merge_list

def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list 
    mid = int(len(my_list)/2)
    left = my_list[:mid]
    right = my_list[mid:]
    return merge(merge_sort(left),merge_sort(right))

print(merge_sort([19,9,0,2,6,8,1]))
