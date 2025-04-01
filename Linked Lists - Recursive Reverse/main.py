class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    if not head or not head.next:
        return head

    tail = reverse(head.next)
    head.next.next = head
    head.next = None

    return tail
