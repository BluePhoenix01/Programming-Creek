class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, values = None):
        if not values:
            self.head = None
        else:
            self.head = Node(values[0])
            current = self.head
            for value in values[1:]:
                current.next = Node(value)
                current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

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

# print("Example usage:")
# ll = LinkedList([1, 2, 3, 4, 5])
# iterator = ReverseLinkedListIterator(ll.head)
# while iterator.hasNext():
#     print(iterator.next(), end=" ")