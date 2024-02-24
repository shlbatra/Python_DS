# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Use slow and fast pointer approach where fast pointer is twice as fast as slow pointer
        Till the time fast pointer gets to end, slow pointer will be in the middle of LL
        '''
        slow=fast=head
        
        while fast and fast.next is not None:
            slow=slow.next 
            fast=fast.next.next
        return slow

    def middleNode_slow(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        First calculate len of linked list
        Middle node will be len(LL)/2 - use as another loop to return middle of LL
        '''
        temp=head
        ll_len=0
        while temp is not None:
            ll_len+=1
            temp=temp.next 
        
        counter=ll_len//2
        node=head    
        for i in range(counter):
            node=node.next
        return node