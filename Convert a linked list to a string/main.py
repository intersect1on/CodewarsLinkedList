class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    if not isinstance(node, Node):
        return 'None'

    res = [str(node.data)]

    while node.next:
        node = node.next
        res.append(str(node.data))

    return ' -> '.join(res + ['None'])
