from Extra_linked_list import LinkedList, Node

def partition(head, x):
    if not head:
        return None

    # Dummy node helps handle cases where head itself is moved
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    current = head

    # `left` will always point to the last node < x
    left = dummy

    while current:
        if current.value < x:
            if left == prev:  
                # left and prev are aligned; just advance all
                left = current
                prev = current
                current = current.next
            else:
                # Remove current from its place
                prev.next = current.next

                # Insert current after left
                current.next = left.next
                left.next = current
                left = current  # update left

                # Move current forward (prev stays the same!)
                current = prev.next
        else:
            prev = current
            current = current.next

    return dummy.next

print("Original list:")
list1 = LinkedList([1, 4, 3, 2, 5, 2])
list1.print_list()
print("Partitioned list:")
partition(list1.head, 3)
list1.print_list()