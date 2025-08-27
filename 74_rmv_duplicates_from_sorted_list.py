from Extra_linked_list import LinkedList

def removeDuplicates(head):
    current = head
    while current and current.next:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next
    return head

print("Remove Duplicates from Sorted List")
head = LinkedList([1, 1, 2, 3, 3]).head
head = removeDuplicates(head)
while head:
    print(head.value, end=" ")
    head = head.next