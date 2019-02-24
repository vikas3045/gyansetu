from linkedlist import *


def is_palindrome(head):
    reversed_list = reverse_list(head)
    return are_equal(head, reversed_list)


def are_equal(headA, headB):
    while headA != None and headB != None:
        if headA.data != headB.data:
            return False

        headA = headA.next
        headB = headB.next
    
    return headA == None and headB == None


def reverse_and_clone(head):
    clone_head = None
    current = head

    while current != None:
        clone_head = Node()
        current = current.next

    if head == None:
        return None

    if head.next == None:
        return head

    second_node = head.next
    reversed_list = reverse_list(second_node)
    second_node.next = head
    head.next = None

    return reversed_list


""" Driver code """

head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(2)
fifth = Node(1)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

#head = create_list()

print_list(head)

print(is_palindrome(head))