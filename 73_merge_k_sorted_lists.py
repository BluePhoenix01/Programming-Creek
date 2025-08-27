from Extra_linked_list import Node, LinkedList
import heapq

def mergeKLists(lists):
    dummy = Node(0)     # dummy start node
    current = dummy
    min_heap = []

    # push first node of each list into heap
    for idx, l in enumerate(lists):
        current_l = l.head
        if current_l:
            heapq.heappush(min_heap, (current_l.value, idx, current_l))  # 👈 idx avoids comparison error

    while min_heap:
        val, idx, node = heapq.heappop(min_heap)
        current.next = Node(val)
        current = current.next
        if node.next:
            heapq.heappush(min_heap, (node.next.value, idx, node.next))

    # wrap in LinkedList if you want consistency
    merged = LinkedList()
    merged.head = dummy.next
    return merged.head


sorted = mergeKLists([LinkedList([1, 4, 5]), LinkedList([1, 3, 4]), LinkedList([2, 6])])
while sorted:
    print(sorted.value, end=" ")
    sorted = sorted.next