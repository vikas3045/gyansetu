from tree import *
from collections import deque
import queue


def visit_node(node):
    print(node.data)

#region Preorder
def preorder(root):
    if root is None:
        return

    stack = [root]

    while len(stack) > 0:
        current = stack.pop()

        visit_node(current)

        if current.right is not None:
            stack.append(current.right)

        if current.left is not None:
            stack.append(current.left)


# def preorder_recursive(root):
#     if root is not None:
#         visit_node(root)
#         preorder_recursive(root.left)
#         preorder_recursive(root.right)


#endregion

#region Inorder

def inorder(root):
    if root is None:
        return

    stack = []
    current = root

    while len(stack) > 0 or current is not None:
        if current is not None:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            visit_node(current)
            current = current.right
        

#endregion
def postorder_recursive(root):
    if root is not None:
        postorder_recursive(root.left)
        postorder_recursive(root.right)
        visit_node(root)

#region Level order
def level_order(root):
    if root is None:
        return
    
    queue = deque([root])

    while len(queue) > 0:
        current = queue.popleft()
        visit_node(current)

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)


def level_order_alt(root):
    height = get_height(root)
    for i in range(1, height+1):
        print_level(root, i)

def print_level(root, level):
    if root is None:
        return

    if level == 1:
        visit_node(root)
    elif level > 1:
        print_level(root.left, level-1)
        print_level(root.right, level-1)


def get_height(root):
    if root is None:
        return 0
    
    left_height = get_height(root.left)
    right_height = get_height(root.right)

    return max(left_height, right_height) + 1


def level_order_null_delim(root):
    if root is None:
        return

    queue = deque([root])
    queue.append(None)

    #or queue = deque([root, None])

    while len(queue) > 0:
        current = queue.popleft()

        if current is not None:
            visit_node(current)

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)
        else:
            if len(queue) != 0:
                queue.append(None)

            # Any operation that needs to be done at level end
            print('Level end')


#endregion



""" Driver code """

root = create_tree()
#preorder(root)
#postorder_recursive(root)
#inorder(root)
#level_order(root)
level_order_alt(root)
level_order_null_delim(root)
