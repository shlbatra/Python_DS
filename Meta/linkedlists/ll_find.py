# Take a linked list and target
# Return true if tgt contained in LL else False

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

class LL_Find:
    def ll_find_tgt_traversal(self, head, tgt): # Space O(1)
        curr = head
        while curr is not None:
            if curr.value == tgt:
                return True
            curr = curr.next
        return False

    def ll_find_tgt_recursive(self, head, tgt): # Space O(n) for n recursive fn calls

        if head is None: return False # base case if get to end of linked list
        if head.value == tgt: return True # base case if match tgt

        return self.ll_find_tgt_recursive(head.next, tgt)

ll = LL_Find()
ans1 = ll.ll_find_tgt_traversal(a, 'C')
print(ans1)
ans2 = ll.ll_find_tgt_traversal(a, 'E')
print(ans2)
ans1 = ll.ll_find_tgt_recursive(a, 'C')
print(ans1)
ans2 = ll.ll_find_tgt_recursive(a, 'E')
print(ans2)
