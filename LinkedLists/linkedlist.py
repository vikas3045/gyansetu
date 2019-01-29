class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, nextNode):
        self.next = nextNode

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next != None


def list_length(node):
    current = node
    count = 0

    while current != None:
        count += 1
        current = current.get_next()

    return count


def insert_at_begining(head, data):
    nodeToBeAdded = Node()
    nodeToBeAdded.data = data

    if head != None:
        nodeToBeAdded.next = head

    head = nodeToBeAdded
    return head


def insert_at_pos(head, pos, data):
    listLength = list_length(head)

    if listLength < pos or pos < 0:
        return None
    elif listLength == pos:
        insert_at_end(head, data)
    else:
        nodeToBeAdded = Node()
        nodeToBeAdded.data = data

        count = 1
        current = head

        while count < pos-1:
            count += 1
            current = current.next()

        nodeToBeAdded.set_next(current.get_next())
        current.set_next(nodeToBeAdded)


def insert_at_end(head, data):
    pass


head = Node()
head.set_data(1)

secondNode = Node()
secondNode.set_data(2)

head.set_next(secondNode)

print(list_length(head))

head = insert_at_begining(head, 0)

print(list_length(head))

insert_at_pos(head, 1, 6)

print(list_length(head))
print(head.get_data())
