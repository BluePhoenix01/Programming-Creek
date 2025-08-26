from Extra_linked_list import Node

def mergeTwoLists(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # Append any remaining nodes from either list
    tail.next = l1 if l1 else l2

    return dummy.next

# Test case setup
l1 = Node(1)
l1.next = Node(3)
l1.next.next = Node(5)

l2 = Node(2)
l2.next = Node(4)
l2.next.next = Node(6)

merged_head = mergeTwoLists(l1, l2)
while merged_head:
    print(merged_head.value, end=" ")
    merged_head = merged_head.next