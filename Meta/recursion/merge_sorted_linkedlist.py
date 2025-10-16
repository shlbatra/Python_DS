# Merge 2 Linked Lists - can be different lengths (No list empty)
# ex. LL1 1, 5, 6, 9   LL2 0, 3, 4, 8, 9, 10
# O/p -> 0, 1, 3, 4, 6, 8, 9, 9, 10

class LL_Node:
    def __init__(self, value):
        self.value = value
        self.next = None

a = LL_Node(1) 
b = LL_Node(5) 
c = LL_Node(6) 
d = LL_Node(9)
a.next = b
b.next = c
c.next = d


q = LL_Node(0) 
r = LL_Node(3)
s = LL_Node(4)
t = LL_Node(8)
u = LL_Node(9)
v = LL_Node(10)
q.next = r
r.next = s
s.next = t
t.next = u
u.next = v


def merge_sorted_ll_traversal(head1, head2):
    if head1 is None and head2 is None: return None # Base cases for empty lists
    if head1 is None: return head2 
    if head2 is None: return head1

    curr1 = head1
    curr2 = head2

    if curr1.value <= curr2.value:
        head = curr1
        curr1 = curr1.next
    else:
        head = curr2
        curr2 = curr2.next

    tail = head

    while curr1 is not None and curr2 is not None:
        #print(curr1.value)
        #print(curr2.value)
        if curr1.value <= curr2.value:
            tail.next = curr1
            tail = curr1
            curr1 = curr1.next
        elif curr1.value > curr2.value:
            tail.next = curr2
            tail = curr2
            curr2 = curr2.next

    if curr1 is not None:
        tail.next = curr1
    if curr2 is not None:
        tail.next = curr2

    return head

def merge_sorted_ll_recursive(head1, head2):

    # Base cases
    if head1 is None and head2 is None: return None
    if head1 is None: return head2
    if head2 is None: return head1

    if head1.value <= head2.value:
        head1.next = merge_sorted_ll_recursive(head1.next, head2)
        return head1
    if head1.value > head2.value:
        head2.next = merge_sorted_ll_recursive(head1, head2.next)
        return head2

def ll_recursive(head):
    if head is None: return
    print(head.value)
    return ll_recursive(head.next)

#ans = merge_sorted_ll_traversal(a, q)
ans = merge_sorted_ll_recursive(a, q)
# print(ans.next.value)
ll_recursive(ans)
