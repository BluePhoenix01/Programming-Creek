class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        # Step 1: create mapping
        old_to_new = {}
        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next

        # Step 2: assign next and random
        cur = head
        while cur:
            old_to_new[cur].next = old_to_new.get(cur.next)
            old_to_new[cur].random = old_to_new.get(cur.random)
            cur = cur.next

        # Step 3: return new head
        return old_to_new[head]
    
def print_list(head):
    curr = head
    res = []
    while curr:
        rand_val = curr.random.val if curr.random else None
        res.append(f"({curr.val}, rand={rand_val})")
        curr = curr.next
    print(" -> ".join(res))

# Test case setup
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.next = n2
n2.next = n3

n1.random = n3   # 1 → 3
n2.random = n1   # 2 → 1
n3.random = n3   # 3 → itself

print("Original List:")
print_list(n1)

# suppose you call your copy function here
solution = Solution()
copied_head = solution.copyRandomList(n1)

print("Copied List:")
print_list(copied_head)