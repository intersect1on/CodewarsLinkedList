class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if not head or not head.next:
        raise IndexError

    first = Node(head.data)
    second = Node(head.next.data)
    first_head = first
    second_head = second
    node = head.next.next
    counter = 1

    while node:
        if counter % 2:
            first.next = Node(node.data)
            first = first.next
        else:
            second.next = Node(node.data)
            second = second.next

        node = node.next
        counter += 1

    return Context(first_head, second_head)
