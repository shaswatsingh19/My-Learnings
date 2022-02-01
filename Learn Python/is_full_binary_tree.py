class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def is_full(root):
    if root is None:

        return True

    if root.left is None and root.right is None:
        return True

    if root.left != None and root.right != None :
        return is_full(root.left) and is_full(root.right)

    return False

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
# root.left.right = Node(5)

if is_full(root):
    print("GIVEN TREE IS A FULL BINARY TREE")
else:
    print("NOT A FULL BINARY TREE")

''''
Properties of FULL BINARY TREE

Let, i = the number of internal nodes
       n = be the total number of nodes
       l = number of leaves
      λ = number of levels
The number of leaves is i + 1.
(l = i+1)
The total number of nodes is 2i + 1.
(n=2i+1)
The number of leaves is at most 2λ - 1.
l = (2λ - 1.)


