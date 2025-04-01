class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(s):
    data = s.split(' -> ')[:-1]

    if not len(data):
        return None

    tail = Node(int(data[-1]))
    head = tail
    data = data[:-1]

    while data:
        head = Node(int(data[-1]), head)
        data = data[:-1]

    return head
