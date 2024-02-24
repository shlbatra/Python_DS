# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast=head,head.next
        #Beginning of second half - slow.next 
        while fast and fast.next:
            slow=slow.next 
            fast=fast.next.next
        #Reverse second half of the list
        second=slow.next 
        slow.next=None 
        prev=None
       
        while second is not None:
            temp=second.next
            second.next=prev
            prev=second
            second=temp
            
        #merge two halfs 
        first, second=head, prev 
        while second:
            tmp1,tmp2=first.next,second.next 
            first.next = second 
            second.next = tmp1
            first=tmp1
            second=tmp2