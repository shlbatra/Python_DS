class LL_Node:
    def __init__(self, value):
        self.value = value
        self.next = None

a = LL_Node(2) 
b = LL_Node(8) 
c = LL_Node(3) 
d = LL_Node(7)

a.next = b
b.next = c
c.next = d

class LL_Sum:

    def ll_sum_iterative(self, head): # space O(1) - use handful of variables
        total = 0
        curr = head
        while curr is not None:
            total += curr.value
            curr = curr.next
        return total

    def ll_sum_recursive(self, head): # Space O(n) because of n call stack fn calls

        if head is None: return 0

        return head.value + self.ll_sum_recursive(head.next)

ls = LL_Sum()
ans = ls.ll_sum_iterative(a)
print(ans)
ans = ls.ll_sum_recursive(a)
print(ans)