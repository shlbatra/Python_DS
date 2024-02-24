class Node:
    def __init__(self,value):
        self.value = value 
        self.left = None 
        self.right = None 

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self,head,value):
            if head is None:
                new_node = Node(value)
                return new_node

            if head.value < value:
                head.right = self.insert(head.right,value)
            else:
                head.left = self.insert(head.left,value)
            return head

    def print_tree(self,head):
            if head is None:
                return
            #Check node is leaf node
            if head.left is None and head.right is None:
                print(head.value)

            if head.left is not None:
                self.print_tree(head.left)
            
            if head.right is not None:
                self.print_tree(head.right)

                


my_tree = BinarySearchTree()
my_tree.root=my_tree.insert(my_tree.root,4)
my_tree.root=my_tree.insert(my_tree.root,2)
my_tree.root=my_tree.insert(my_tree.root,6)
my_tree.root=my_tree.insert(my_tree.root,1)
my_tree.root=my_tree.insert(my_tree.root,3)
my_tree.root=my_tree.insert(my_tree.root,5)
my_tree.root=my_tree.insert(my_tree.root,7)
my_tree.print_tree(my_tree.root)
#print(my_tree.root.value)
#print(my_tree.root.left.value)
#print(my_tree.root.right.value)