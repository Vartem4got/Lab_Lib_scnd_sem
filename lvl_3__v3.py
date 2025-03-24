# -*- coding: utf-8 -*-



class BinaryTree:
    def __init__(self, val, lft=None, rght=None, parent=None):
        self.val = val
        self.lft = lft
        self.rght = rght
        self.parent = parent

def find_successor(tree: BinaryTree, node: BinaryTree) -> BinaryTree:
    if node.rght:

        successor = node.rght
        while successor.lft:
            successor = successor.lft
        return successor
    

    successor = node.parent
    while successor and node == successor.right:
        node = successor
        successor = successor.parent
    
    return successor


root = BinaryTree(10)
root.lft = BinaryTree(5, parent=root)
root.rght = BinaryTree(15, parent=root)
root.lft.lft = BinaryTree(3, parent=root.lft)
root.lft.rght = BinaryTree(7, parent=root.lft)
root.rght.rght = BinaryTree(20, parent=root.rght)
root.rght.lft = BinaryTree(12, parent=root.rght)


node = root.lft.rght
successor = find_successor(root, node)
print(successor.value if successor else "---")
