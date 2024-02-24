class Node:
    def __init__(self,value):
        self.value=value
        self.next =None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self,node):
        temp = node
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

    def reverse_list(self,head):
            if (head is None or head.next is None):
                return head
            #Recursive approach here 
            p = self.reverse_list(head.next)
            head.next.next=head
            head.next=None
            return p

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
print("List1")
my_linked_list.print_list(my_linked_list.head)
reverse=my_linked_list.reverse_list(my_linked_list.head)
print("Reverse List")
my_linked_list.print_list(reverse)

