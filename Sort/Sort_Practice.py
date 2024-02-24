def bubble_sort_sahil(my_list):
    for i in range(len(my_list)-1):
        for j in range(len(my_list)-i-1):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp 
    return(my_list)

def bubble_sort(my_list):
    for i in range(len(my_list)-1,0,-1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp 
    return(my_list)


def selection_sort(my_list):
    for i in range(len(my_list)-1):
        min_index=i
        for j in range(i+1,len(my_list)):
            if my_list[min_index] > my_list[j]:
                min_index = j
        print(i)
        print(min_index)
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
        print(my_list)
    return(my_list)

def insertion_sort_sahil(my_list):
    for i in range(1,len(my_list)):
        for j in range(i,0,-1):
            if my_list[j] < my_list[j-1]:
                temp = my_list[j]
                my_list[j] = my_list[j-1]
                my_list[j-1] = temp
    print(k)
    return my_list

def insertion_sort(my_list):
    for i in range(1,len(my_list)):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j = j -1  
    return my_list
        
my_list = [1,2,4,3,5,6]
print(insertion_sort_sahil(my_list))
my_list = [1,2,4,3,5,6]
print(insertion_sort(my_list))
#print(bubble_sort(my_list))




