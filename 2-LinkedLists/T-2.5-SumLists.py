from linkedlist import *


def sum_lists(head_a, head_b, carry=0):
    if head_a == None and head_b == None and carry == 0:
        return None
    
    sum = carry

    if head_a != None:
        sum += head_a.data
    if head_b != None:
        sum += head_b.data

    result = Node()
    result.data = sum % 10
    carry = 1 if sum > 9 else 0

    result.next = sum_lists(head_a.next if head_a != None else None, head_b.next if head_b != None else None, carry)

    return result


""" Driver code """

head_a = Node(7)
head_a_second = Node(1)
head_a_third = Node(6)

head_a.next = head_a_second
#head_a_second.next = head_a_third

print_list(head_a)

head_b = Node(5)
head_b_second = Node(9)
head_b_third = Node(2)

head_b.next = head_b_second
head_b_second.next = head_b_third

print_list(head_b)

result = sum_lists(head_a, head_b)

print_list(result)
