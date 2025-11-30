# at most 2 children per node
# exactly 1 root
# exactly 1 path between root and any node (ex. no cycle)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#         a
#     /       \
#     b           c
# /       \           \
# d       e           f