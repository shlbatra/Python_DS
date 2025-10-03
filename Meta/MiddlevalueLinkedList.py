class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next=new_node
            self.tail = new_node
        self.length += 1
        return True

    def mid_of_linked_list(self): -> int:
`       slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next # this moves at twice at speed of slow for slow to get to middle value
        return slow.val

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
print("List1")
my_linked_list.print_list()
my_linked_list.mid_of_linked_list()