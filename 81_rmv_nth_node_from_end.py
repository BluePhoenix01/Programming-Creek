from Extra_linked_list import LinkedList, Node

def rmvNFromEnd(ll, n):
    fast = slow = ll.head
    for _ in range(n):
        if fast is None:
            return
        fast = fast.next
    if fast is None:
        ll.head = ll.head.next
        return
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next

print("Example 1:")
ll = LinkedList([1, 2, 3, 4, 5])
rmvNFromEnd(ll, 2)
ll.print_list()
