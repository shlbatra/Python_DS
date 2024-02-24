def binarysearch(A,left,right,num):
    if left > right:
        return -1

    mid = int((left+right) / 2)

    if num == A[mid]:
        return mid 

    elif num >= A[mid]:
        return binarysearch(A,mid+1,right,num)

    else:
        return binarysearch(A,left,mid-1,num)

lst=[1,2,3,4,5,6]
num=3
print(binarysearch(lst,4,len(lst)-1,num))


