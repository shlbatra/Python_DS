# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        2 Pointer Approach - O(n) and O(1)
        Define two nodes - one prev and one curr
        Move curr ahead and then add reverse link from head to prev
        Increment head to curr
        Make sure you return prev and run it till curr is not None
        '''
        prev=None
        curr=head
        while curr is not None:
            headn=curr.next
            curr.next=prev
            prev=curr
            curr=headn
        return prev

    def reverseList_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Recursive - T-O(n) S-O(n)
        Input HEAD: 1->2->3->null
        At the end of recursive calls 3 becomes newHead and it returns from last recursive call...
        now we have two ways to make 3 point to 2, I will put node value in {} for clarity : 
        A) newHead{3}.next = head{2}

        OR
        B) head{2}.next{3}.next = head{2}

        Now, down the line when it is time for pointing 2 to 1:
        newHead still points to 3 but we can point node 2 to 1 by using 

        head{1}.next{2}.next = head{1}
        '''
        #Base Case
        if head is None:
            return None
        newHead = head
        
        if head.next:
            newHead=self.reverseList(head.next)
            head.next.next=head  #Main step to reverse the list- Hack used here
        head.next=None
        
        return newHead

    def reverseList_recursion_alt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Base Case
        if head is None or head.next is None:
            return head
        
        newHead=self.reverseList(head.next)
        head.next.next=head 
        head.next=None
        
        return newHead
        

    def reverseList_twopointer(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        later=head
        while head is not None:
            later=head.next
            head.next=prev
            prev=head
            head=later
        return prev