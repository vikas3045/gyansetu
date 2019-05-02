def is_balanced(root):
    if root is None:
        return True

    


def get_height(root):
    if root is not None:
        return 0

    left_height = get_height(root.left)
    right_height = get_height(root.right)

    return max(left_height, right_height) + 1
