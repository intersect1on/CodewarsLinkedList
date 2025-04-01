class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    elem = Node(data)

    if not head or data <= head.data:
        elem.next = head
        return elem

    node = head

    while node.next and data > node.next.data:
        node = node.next

    elem.next = node.next
    node.next = elem

    return head
