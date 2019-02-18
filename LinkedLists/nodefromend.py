from linkedlist import *


def nth_node_from_end(head, n):
    if n < 0:
        return None

    current = head
    count = 0

    # Make difference window between two pointers
    while count < n and current != None:
        current = current.next
        count += 1

    # if list doesn't contain n nodes, return None
    if count < n or current == None:
        return None

    p_nth_node = head
    while current.next != None:
        current = current.next
        p_nth_node = p_nth_node.next

    return p_nth_node


""" Driver code """


head = create_list()
print_list(head)

nth_node = nth_node_from_end(head, 5)
print()
print(nth_node.data)
