# Return node value at given index ( With starting index 0 for linked list)

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

class LL_NodeValue:

    def ll_nodevalue_traversal(self, head, index):
        curr = head
        while curr is not None:
            if index == 0:
                return curr.value
            index -= 1
            curr = curr.next
        return None

    def ll_nodevalue_recursive(self, head, index):

        if head is None: return None
        if index == 0: return head.value
        # index -= 1; not reqd if pass as part of fn call below 
        return self.ll_nodevalue_recursive(head.next, index-1)

ll = LL_NodeValue()
ans1 = ll.ll_nodevalue_traversal(a, 3)
print(ans1)
ans2 = ll.ll_nodevalue_traversal(a, 4)
print(ans2)
ans1 = ll.ll_nodevalue_recursive(a, 3)
print(ans1)
ans2 = ll.ll_nodevalue_recursive(a, 4)
print(ans2)