from tree import *


def create_minimal_tree(arr):
    #TODO:check this condition for None input
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return BinaryTreeNode(arr[0])
    else:
        median_idx = get_median_index(arr)

        root = BinaryTreeNode(arr[median_idx])
        left_subtree = create_minimal_tree(arr[:median_idx])
        right_subtree = create_minimal_tree(arr[median_idx+1:])

        root.left = left_subtree
        root.right = right_subtree

        return root


def get_median_index(arr):
    return int((len(arr) - 1)/2)


""" Driver code """


arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 4, 5, 6]

root1 = create_minimal_tree(arr1)
root2 = create_minimal_tree(arr2)