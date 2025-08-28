from Extra_linked_list import Node, LinkedList

def remElems(head, val):
    dummy = Node(0)
    dummy.next = head
    curr = dummy
    while curr.next:
        if curr.next.value == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return dummy.next

print("Remove Linked List Elements")
list1 = LinkedList([1, 2, 6, 3, 4, 5, 6])
list1.head = remElems(list1.head, 6)
list1.print_list()
