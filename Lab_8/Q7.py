'''Implement the binary tree using python'''

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, root, value):
        if value < root.value:
            if root.left is None:
                root.left = Node(value)
            else:
                self._insert(root.left, value)
        elif value > root.value:
            if root.right is None:
                root.right = Node(value)
            else:
                self._insert(root.right, value)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

# Example usage
bt = BinaryTree()
bt.insert(50)
bt.insert(30)
bt.insert(20)
bt.insert(40)
bt.insert(70)
bt.insert(60)
bt.insert(80)

print("Inorder Traversal:")
bt.inorder(bt.root)




# Name : Sanika Patil
# Section K
# 23FE10CSE00445