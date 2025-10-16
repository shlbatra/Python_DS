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

# A -> B -> C -> None
def ll_reversal(head, prev = None):
    if head is None: return prev
    forw = head.next
    head.next = prev
    return ll_reversal(forw, head)

def ll_reversal_alternate(head):

    if head is None or head.next is None:
        return head
    prev = ll_reversal_alternate(head.next)
    head.next.next = head
    head.next = None

    return prev

ans = ll_reversal(a)
print(ans.value)

# ans = ll_reversal_alternate(a)
# print(ans.value)
