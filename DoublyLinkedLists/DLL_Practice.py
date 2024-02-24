class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None 

class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_dll(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next 

    def append(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node 
            self.tail = new_node
        self.length += 1
        return True 

    def pop(self):
        if self.length == 0:
            return None 
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None 
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node 
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node 

        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None 
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None 
        else:
            self.head = self.head.next
            self.head.prev = None 
            temp.next = None 
        self.length -= 1
        return temp 

    def get(self,index):
        if index<0 or index >= self.length :
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
            #for _ in range(self.length -index -1)
                temp = temp.prev
        return temp

    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        else:
            return False

    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False 
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            before = self.get(index-1)
            after = before.next   #O(1)
            new_node.prev = before 
            new_node.next = after
            before.next = new_node
            after.prev = new_node
            self.length+=1
            return True 

    def remove(self,index):
        if index<0 or index>=self.length:
            return False 
        elif index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        else:
            temp =self.get(index)
            temp.next.prev = temp.prev 
            temp.prev.next = temp.next 
            temp.next = None
            temp.prev = None 
            self.length -=1
            return temp


print("List1")
my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)
my_dll.print_dll()
print("List3")
my_dll.prepend(0)
my_dll.print_dll()
print("Remove")
print(my_dll.remove(2))
print(my_dll.remove(0))
my_dll.print_dll()