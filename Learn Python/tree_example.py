from tree_traversal import *

root = Node("F")
root.left = Node("B")
root.left.left = Node("A")
root.left.right = Node("D")
root.left.right.left  = Node("C")
root.left.right.right = Node("E")

root.right = Node("G")
root.right.right = Node("I")
root.right.right.left = Node("H")

print("Inorder traversal ")
in_order(root)

print("\nPreorder traversal ")
pre_order(root)

print("\nPostorder traversal ")
post_order(root)
'''
Inorder traversal 
A --> B --> C --> D --> E --> F --> G --> H --> I --> 
Preorder traversal 
F --> B --> A --> D --> C --> E --> G --> I --> H --> 
Postorder traversal 
A --> C --> E --> D --> B --> H --> I --> G --> F -->
'''
