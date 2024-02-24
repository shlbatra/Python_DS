def merge(list1,list2):
    res=[]
    i=0
    j=0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            res.append(list1[i])
            i=i+1
        else:
            res.append(list2[j])
            j=j+1

    while i < len(list1):
        res.append(list1[i])
        i = i + 1

    while j < len(list2):
        res.append(list2[j])
        j = j + 1

    return res
    
def merge_sort(lst):
    if len(lst) == 1:
        return lst
    mid=int(len(lst)/2)
    left = lst[:mid]
    right = lst[mid:]
    return merge(merge_sort(left),merge_sort(right))

#input=[2,6,3,6,1,0]
#print(merge_sort(input))


def merge_alt(data,start,mid,end):
    temp=[]
    i=start
    j=mid+1

    while (i <=mid and j<=end):
        if data[i] <= data[j]:
            temp.append(data[i])
            i=i+1
        else:
            temp.append(data[j])
            j=j+1

    while i<=mid:
        temp.append(data[i])
        i=i+1

    while j<=end:
        temp.append(data[j])
        j=j+1

    for i in range(start,end):
        data[i]=temp[i-start]

def merge_sort_alt(data,start,end):
    if (start < end):
        mid = int((start+end)/2)
        merge_sort_alt(data,start,mid)
        merge_sort_alt(data,mid+1,end)
        merge_alt(data,start,mid,end)

input=[2,6,3,6,1,0]
print(input)
merge_sort_alt(input,0,len(input)-1)
print(input)
