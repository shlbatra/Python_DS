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

def merge_list(head1,head2):
            if (head1 is None):
                return head2
            if (head2 is None):
                return head1
            #Recursive approach here 
            if (head1.value < head2.value):
                head1.next=merge_list(head1.next,head2)
                return head1
            else: 
                head2.next=merge_list(head1,head2.next)
                return head2

def print_list_final(node):
        temp = node
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_linked_list1 = LinkedList(1)
my_linked_list1.append(3)
my_linked_list1.append(5)
my_linked_list1.append(7)
print("List1")
my_linked_list1.print_list(my_linked_list1.head)

my_linked_list2 = LinkedList(2)
my_linked_list2.append(4)
my_linked_list2.append(6)
my_linked_list2.append(8)
print("List2")
my_linked_list2.print_list(my_linked_list2.head)

merged=merge_list(my_linked_list1.head,my_linked_list2.head)
print("merged")
print_list_final(merged)

