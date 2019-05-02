from linkedlist import *


def delete_middle_node(node):
    if node == None or node.next == None:
        return
    
    next = node.next
    node.data = next.data
    node.next = next.next

