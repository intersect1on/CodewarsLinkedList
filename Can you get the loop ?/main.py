class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def loop_size(node):
    if not node.next:
        return 0

    slow = node
    fast = node

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            slow = slow.next
            length = 1

            while slow != fast:
                slow = slow.next
                length += 1

            return length

    return 0
