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


###############################################


def list_length(head):
    current = head
    count = 0

    while current != None:
        current = current.next
        count += 1

    return count


def insert_at_begining(head, data):
    node = Node(data)

    if head == None:
        head = node
    else:
        node.next = head
        head = node

    return head


def insert_at_end(head, data):
    node = Node(data)

    if head == None:
        head = node
    else:
        current = head
        while current.next != None:
            current = current.next
        current.next = node


def create_list(n=10):
    head = Node(1)

    for i in range(2, n+1):
        insert_at_end(head, i)

    return head


def create_cyclic_list(n=10):
    head = create_list(n)
    current = head
    count = 0
    cyclic_node = None

    while current.next != None:
        count += 1
        if count == 7:
            cyclic_node = current
        current = current.next

    current.next = cyclic_node
    return head


def print_list(head):
    current = head

    while current != None:
        print(' ' + str(current.data), end=' >')
        current = current.next


#####################################################
""" Driver code """
#####################################################

# head = Node()
# head.data = 1

# second_node = Node()
# second_node.data = 2

# head.next = second_node

# head = insert_at_begining(head, 99)
# insert_at_end(head, 4)


# print(list_length(head))
# print(head.data)
# print_list(head)
