class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, values=None):
        if values is None:
            self.head = None
        else:
            self.head = Node(values[0])
            current = self.head
            for v in values[1:]:
                current.next = Node(v)
                current = current.next

    def hasCycle(self):
        slow = fast = self.head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
print("Example usage:")
ll = LinkedList([1, 2, 3, 4, 5])
print("Has cycle:", ll.hasCycle())
ll_with_cycle = LinkedList([1, 2, 3, 4, 5])
ll_with_cycle.head.next.next.next.next = ll_with_cycle.head.next
print("Has cycle:", ll_with_cycle.hasCycle())