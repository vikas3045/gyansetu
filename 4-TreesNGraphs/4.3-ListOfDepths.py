class Node:
    def __init__(self, data=None, next_node=None):
        self._data = data
        self._next = next_node

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_node):
        self._next = next_node

    def has_next(self):
        return self.next != None



from tree import *
from collections import deque


def get_lists_of_depths(root):
    if root is None:
        return

    dict_depths = dict()
    q = deque([root])
    q.append(None)

    dict_depths[1] = Node(root.data)
    depth = 1
    ll = LinkedList()

    while len(q) > 0:
        current = q.popleft()
       
        if current is not None:

            if current.left is not None:
                q.append(current.left)
                ll.append(current.left.data)

            if current.right is not None:
                q.append(current.right)
                ll.append(current.right.data)

        else:
            if len(q) != 0:
                q.append(None)
            
            depth += 1
            dict_depths[depth] = ll.head
            ll.head = None
    
    return dict_depths


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        if self.head is not None:
            current = self.head
            while current.next is not None:
                current = current.next
            
            current.next = Node(data)
        else:
            self.head = Node(data)



""" Driver code """

root = create_tree()
d = get_lists_of_depths(root)



