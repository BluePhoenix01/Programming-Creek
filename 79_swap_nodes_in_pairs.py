from Extra_linked_list import Node, LinkedList

def swapPairs(head):
    dummy = Node(0)
    dummy.next = head
    current = dummy
    while current.next and current.next.next:
        first = current.next
        second = current.next.next
        first.next = second.next
        second.next = first
        current.next = second
        current = first
    return dummy.next

list1 = LinkedList([1, 2, 3, 4])
list1.head = swapPairs(list1.head)
list1.print_list()