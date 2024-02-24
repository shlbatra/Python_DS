# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Create a dumy node that will point to the sorted linked list
        Loop through the linkedlist and add smaller value from list
        Make sure the seperate linkedlists are moved forward and tail move forwards
        Append remaining lists and retunr dummy.next 
        '''
        
        dummy=ListNode() #Create dumy node for empty list edge case
        tail=dummy
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                tail.next=list1
                list1 = list1.next
            else:
                tail.next=list2
                list2 = list2.next
            tail=tail.next
        if list1:
            tail.next=list1
        elif list2:
            tail.next=list2
        return dummy.next

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Recursive Solution 
        Base Condition -> Both lists not at None stage, If None, return the other list
        Keep iterating through list and call recursively with the next of smaller value and other list value
        '''
        def mergeLists(list1,list2):
            if list1 is None:
                return list2
            elif list2 is None:
                return list1

            if (list1.val < list2.val):
                list1.next=mergeLists(list1.next,list2)
                return list1
            else:
                list2.next=mergeLists(list1,list2.next)  
                return list2
        return mergeLists(list1,list2)