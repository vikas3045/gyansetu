from linkedlist import *


def kth_node_to_last(head, k):
    if k < 0:
        return None

    current = head
    kth_node = head
    count = 0

    while current != None and count < k:
        current = current.next
        count += 1

    if current == None or count < k:
        return None

    while current != None:
        current = current.next
        kth_node = kth_node.next
    
    return kth_node
    