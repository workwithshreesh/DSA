class DoublyListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, val):
        new_node = DoublyListNode(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def print_forward(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

    def print_backward(self):
        current = self.tail
        while current:
            print(current.val, end=" -> ")
            current = current.prev
        print("None")

# Example usage:
doubly_linked_list = DoublyLinkedList()

# Insert elements at the end of the doubly linked list
doubly_linked_list.insert_at_end(4)
doubly_linked_list.insert_at_end(2)
doubly_linked_list.insert_at_end(1)
doubly_linked_list.insert_at_end(3)

# Print the doubly linked list in forward and backward directions
print("Forward:")
doubly_linked_list.print_forward()

print("\nBackward:")
doubly_linked_list.print_backward()
