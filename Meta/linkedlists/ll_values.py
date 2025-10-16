class LL_Node:
    def __init__(self, value):
        self.value = value
        self.next = None

a = LL_Node('A') 
b = LL_Node('B') 
c = LL_Node('C') 
d = LL_Node('D')

a.next = b
b.next = c
c.next = d

class LL_Values:
    def ll_values_array(self, head):
        arr = []
        curr = head
        while curr is not None:
            arr.append(curr.value)
            curr = curr.next

        return arr

    def ll_values_array_recursive(self, head):
        
        def fillValues(head, arr):

            if head is None: return # base case
            arr.append(head.value) 
            fillValues(head.next, arr)
            #return arr # return after all recursive calls complete but will be O(N2)
        arr = []
        fillValues(head, arr)
        return arr
        

lv = LL_Values()
arr = lv.ll_values_array(a)
print(arr)
arr = lv.ll_values_array_recursive(a)
print(arr)