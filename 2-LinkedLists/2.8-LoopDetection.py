from linkedlist import *


def get_loop_start_node(head):
    slw_ptr = fst_ptr = head
    is_loop_present = False

    while fst_ptr and fst_ptr.next:     
        fst_ptr = fst_ptr.next.next
        slw_ptr = slw_ptr.next

        # TBD - Study difference between is and ==
        if fst_ptr == slw_ptr:
            is_loop_present = True
            break

    if is_loop_present:
        fst_ptr = head

        while fst_ptr != slw_ptr:
            fst_ptr = fst_ptr.next
            slw_ptr = slw_ptr.next

    return fst_ptr

