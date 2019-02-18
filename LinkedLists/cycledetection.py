from linkedlist import *


def get_loop_node(head):
    slw_ptr = head
    fst_ptr = head
    is_loop_present = False

    while fst_ptr != None and fst_ptr.next != None:
        slw_ptr = slw_ptr.next
        fst_ptr = fst_ptr.next.next

        if slw_ptr == fst_ptr:
            is_loop_present = True
            break

    if is_loop_present:
        fst_ptr = head
        while slw_ptr != fst_ptr:
            slw_ptr = slw_ptr.next
            fst_ptr = fst_ptr.next

    return fst_ptr


""" Driver code """


head = create_cyclic_list()

loop_node = get_loop_node(head)

print(loop_node.data)
