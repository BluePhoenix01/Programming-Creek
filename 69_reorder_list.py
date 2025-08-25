class Node:
    def __init__(self, value = 0, next = None):
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

    def lenOfList(self):
        current, length = self.head, 0
        while current:
            length += 1
            current = current.next
        return length

    def revList(self, head):
        prev, current = None, head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev  # return new head

    def reorderList(self):
        if not self.head or not self.head.next:
            return

        # Step 1: find middle (slow will be at mid)
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: reverse second half
        second = self.revList(slow.next)
        slow.next = None

        # Step 3: merge two halves
        first = self.head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
    def printList(self):
        current = self.head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next

l1 = LinkedList([1,2,3,4,5])
l1.reorderList()
l1.printList()  # Output: 1 -> 5 -> 2 -> 4 -> 3 ->