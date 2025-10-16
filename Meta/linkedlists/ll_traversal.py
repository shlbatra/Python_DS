class LL_Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LL_Traversal:
    def print_ll(self, head):
        current = head
        while current is not None:
            print(current.value)
            current = current.next

    def print_ll_recursive(self, head):
        if head is None: return # base case
        print(head.value)
        return self.print_ll_recursive(head.next)

a = LL_Node('A') 
b = LL_Node('B') 
c = LL_Node('C') 
d = LL_Node('D')

a.next = b
b.next = c
c.next = d

# A -> B -> C -> D -> Null

p = LL_Traversal()
p.print_ll(a)
p.print_ll_recursive(a)