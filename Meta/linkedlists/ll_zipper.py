# Combine 2 Linked Lists - can be different lengths (No list empty)
# ex. LL1 A, B, C, D.   LL2 E, F, G, H, I
# O/p -> A, E, B, F, C, G, D, H, I

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


q = LL_Node('Q') 
r = LL_Node('R') 
q.next = r

class LL_Zipper:
    def ll_zipper(self, head1, head2):
        curr1 = head1.next
        curr2 = head2
        tail = head1
        count=0
        while curr1 is not None and curr2 is not None:
            if count % 2 == 0:
                tail.next = curr2
                curr2 = curr2.next
            else:
                tail.next = curr1
                curr1 = curr1.next
            tail = tail.next
            count += 1

        if curr1 is not None:
            tail.next = curr1

        if curr2 is not None:
            tail.next = curr2

        return head1

    def ll_zipper_recursive(self, head1, head2):

        if head1 is None and head2 is None: return None
        if head1 is None: return head2  # Leftover longer list
        if head2 is None: return head1

        next1 = head1.next
        next2 = head2.next
        head1.next = head2
        head2.next = self.ll_zipper_recursive(next1, next2)
        return head1

    def ll_recursive(self, head):
        if head is None: return
        print(head.value)
        return self.ll_traversal(head.next)

    def ll_traversal(self, head):
        current = head
        while current is not None:
            print(current.value)
            current = current.next

ll =  LL_Zipper()
# ans = ll.ll_zipper_recursive(a, q)
ans = ll.ll_zipper(a, q)
ll.ll_traversal(ans)








