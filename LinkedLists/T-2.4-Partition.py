from linkedlist import *


def partition(head, x):
    new_head = None
    current = head

    while current != None:
        
        if current.data <= x:
            new_head = insert_at_begining(new_head, current.data)
        else:
            insert_at_end(new_head, current.data)
        
        current = current.next

    return new_head


""" Driver code """
head = Node(10)
second_node = Node(1)
third_node = Node(15)
fourth_node = Node(3)

head.next = second_node
second_node.next = third_node
third_node.next = fourth_node

print_list(head)

head = partition(head, 5)

print_list(head)



