from linkedlist import *


class Stack:
    def __init__(self, data=None):
        self.head = None
        if data:
            for data in data:
                self.push(data)

    def push(self, data):
        node = Node(data, self.head)
        self.head = node

    def pop(self):
        if self.head is None:
            raise IndexError

        node_data = self.head.data
        self.head = self.head.next
        return node_data

    def peek(self):
        if self.head is None:
            raise IndexError

        return self.head.data

""" Driver code """

# lst = [1, 2, 3, 4]
# stack = Stack(lst)

# print(stack.pop())
# print(stack.peek())


