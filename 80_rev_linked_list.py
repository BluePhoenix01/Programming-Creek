class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, values=None):
        if not values:
            self.head = None
        else:
            self.head = Node(values[0])
            current = self.head
            for value in values[1:]:
                current.next = Node(value)
                current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
    
ll = LinkedList([1, 2, 3, 4, 5])

print("Reversing the linked list:")

ll.reverse()
ll.print_list()