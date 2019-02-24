from linkedlist import *


def remove_dups(head):
    prev = None
    current = head
    node_set = set()
    
    while current != None:

        if current.data in node_set:
            prev.next = current.next        
        else:            
            node_set.add(current.data)
            prev = current

        current = current.next

def remove_dups_no_buffer(head):
    pass

""" Driver code """
head = create_list()
node = Node(1)
node.next = head
head = node

print_list(head)

remove_dups(head)

print_list(head)
