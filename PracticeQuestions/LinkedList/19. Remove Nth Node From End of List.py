# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        Use two pointer approach 
        Left will be pointing at dumy before head and right will be at head
        Right initially will move by k steps ahead
        Then Move both left and right till right is None
        Finally, delete node by adding left.next = left.next.next
        '''
        dummy=ListNode(0,head)
        left,right=dummy,head
        while n > 0 and right is not None:
            right=right.next 
            n=n-1
        while right:
            left=left.next 
            right=right.next 
        #delete node
        left.next=left.next.next 
        return dummy.next