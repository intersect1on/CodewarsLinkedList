class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    node = head
    temp = Node()
    temp.next = head
    prev_node = temp

    while node and node.next:
        first_node = node
        second_node = node.next
        next_node = second_node.next
        prev_node.next = second_node
        second_node.next = first_node
        first_node.next = next_node
        prev_node = first_node
        node = next_node

    return temp.next
