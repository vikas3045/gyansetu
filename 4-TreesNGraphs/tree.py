class BinaryTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BSTNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def create_tree():
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)

    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)

    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)

    return root