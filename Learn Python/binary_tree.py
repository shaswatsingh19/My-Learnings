class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    # Traverse preorder
    def traverse_pre_order(self):
        print(self.data, end=' ')
        if self.left:
            self.left.traverse_pre_order()
        if self.right:
            self.right.traverse_pre_order()

    # Traverse inorder
    def traverse_in_order(self):
        if self.left:
            self.left.traverse_in_order()
        print(self.data, end=' ')
        if self.right:
            self.right.traverse_in_order()

    # Traverse postorder
    def traverse_post_order(self):
        if self.left:
            self.left.traverse_post_order()
        if self.right:
            self.right.traverse_post_order()
        print(self.data, end=' ')


root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)

print("Pre order Traversal: ", end="")
root.traverse_pre_order()
print("\nIn order Traversal: ", end="")
root.traverse_in_order()
print("\nPost order Traversal: ", end="")
root.traverse_post_order()

'''
Pre order Traversal: 1 2 4 3 
In order Traversal: 4 2 1 3 
Post order Traversal: 4 2 3 1
'''
