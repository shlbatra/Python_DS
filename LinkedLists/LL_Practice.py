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

    def pop(self):
        #print(f"Length :  {self.length}")
        if self.length==0:
            temp = None
        elif self.length==1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            pre=self.head
            temp = self.head
            while temp.next is not None:
                pre=temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
        return temp

    def prepend(self,value):
        new_node = Node(value)
        if self.length ==0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            
        self.length += 1
        return True

    def pop_first(self):
        if self.length ==0:
            temp = None
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.length -= 1  
            if self.length == 0:
                self.tail = None
        return temp

    def get(self, index):
        
        if index<0 or index >= self.length :
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    def set_value(self, index,value):

        temp = self.get(index)

        if temp is None:
            return False
        else:
            temp.value=value
            return True
            
    def insert(self,index,value):
        if index<0 or index > self.length :
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            temp = self.get(index-1)
            new_node.next = temp.next
            temp.next = new_node
            self.length +=1
            return True

    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        else:
            prev = self.get(index-1)
            temp = prev.next
            prev.next = temp.next 
            temp.next = None
            self.length -= 1
            return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = self.head
        before = None 
        after = temp.next 
        for _ in range(self.length):
            after = temp.next  # 7 ; 2 
            temp.next = before  # None ; 1 
            before = temp # 1 ; 7
            temp = after # 7 ; 2

    def reverse_alt(self):
        prev=None
        curr=self.head
        temp = self.head
        self.head = self.tail
        self.tail = self.head
        while curr is not None:
            headn=curr.next
            curr.next=prev
            prev=curr
            curr=headn
        
        
         
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
print("List1")
my_linked_list.print_list()
my_linked_list.pop()
print("List2")
my_linked_list.print_list()
my_linked_list.prepend(0)
print("List3")
my_linked_list.print_list()
print("List4")
my_linked_list.pop_first()
my_linked_list.print_list()
print("Insert Item")
my_linked_list.insert(1,7)
my_linked_list.print_list()
print("Remove Item")
print(my_linked_list.remove(4))
my_linked_list.print_list()
print("Reverse List")
my_linked_list.reverse_alt()
my_linked_list.print_list()



'''
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next 
        before = None
        for _ in range(self.length):
            after = temp.next 
            temp.next = before 
            before = temp
            temp = after  
'''