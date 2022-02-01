class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def pre_order(root):
    if root != None:
        print(root.data,"-->",end=' ')
        pre_order(root.left)
        pre_order(root.right)


def in_order(root):
    if root:
        in_order(root.left)
        print(root.data,"-->",end=' ')
        in_order(root.right)

def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.data,"-->",end=' ')

'''

root = Node(1)
root.left = Node(12)
root.right = Node(9)
root.left.left = Node(5)
root.left.right = Node(6)


print("Inorder traversal ")
in_order(root)

print("\nPreorder traversal ")
pre_order(root)

print("\nPostorder traversal ")
post_order(root)


Inorder traversal 
5 --> 12 --> 6 --> 1 --> 9 --> 
Preorder traversal 
1 --> 12 --> 5 --> 6 --> 9 --> 
Postorder traversal 
5 --> 6 --> 12 --> 9 --> 1 -->

'''
