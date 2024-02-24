# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle_hashmap(self, head: Optional[ListNode]) -> bool:
        '''
        Using dict to keep track of nodes visited
        '''
        dict_visited={}
        while head is not None:
            if head in dict_visited:
                return True
            dict_visited[head]=1
            head = head.next
        return False

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        Using dict to keep track of nodes visited
        '''
        dict_visited={}
        while head is not None:
            if head in dict_visited:
                return True
            dict_visited[head]=1
            head = head.next
        return False

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast=head,head
        while fast and fast.next is not None:
            slow=slow.next 
            fast=fast.next.next
            if slow == fast:
                return True
        return False