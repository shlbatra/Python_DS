# Reverse Linked List and return new head of linked list
# Ex. return D below

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

class LL_Reverse:
    def ll_reverse_treversal(self, head): # space O(1) as need fixed number of variables
        # Need 2 ptrs prev and next
        prev = None
        curr = head
        # None A -> B -> C
        while curr is not None:
            forw = curr.next
            curr.next = prev #  Null <- A  B
             # Null <- A <- B
            prev = curr
            curr = forw

        return prev.value

    def ll_reverse_recursion(self, head, prev = None):

        if head is None: return prev.value
        forw = head.next
        head.next = prev # Follow along the same code as in traversal
        return self.ll_reverse_recursion(forw, head)

ll = LL_Reverse()
# ans = ll.ll_reverse_treversal(a)
# print(ans)

ans = ll.ll_reverse_recursion(a)
print(ans)