class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def get_nth(node, index):
    if node is None or index < 0:
        raise IndexError

    while index:
        node = node.next
        index -= 1

    if node is None:
        raise IndexError

    return node
