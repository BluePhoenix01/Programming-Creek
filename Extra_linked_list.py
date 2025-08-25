class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, values = None):
        self.head = Node(values[0]) if values else None
        current = self.head
        for value in values[1:]:
            current.next = Node(value)
            current = current.next

class ReverseLinkedListIterator:
    def __init__(self, head):
        # collect all nodes into a stack
        self.stack = []
        current = head
        while current:
            self.stack.append(current.value)
            current = current.next

    def hasNext(self):
        return len(self.stack) > 0

    def next(self):
        if not self.hasNext():
            return None
        return self.stack.pop()  

print("Example usage:")
ll = LinkedList([1, 2, 3, 4, 5])
iterator = ReverseLinkedListIterator(ll.head)
while iterator.hasNext():
    print(iterator.next(), end=" ")