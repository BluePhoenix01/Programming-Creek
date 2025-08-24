class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
    
class LinkedList:
    def __init__(self, list = None):
        if list is None:
            self.head = None
        else:
            self.head = Node(list[0])
            current = self.head
            for value in list[1:]:
                current.next = Node(value)
                current = current.next

    def addTwoNumbers(self, l2):
        current1 = self.head
        current2 = l2.head
        carry = 0
        result = LinkedList()
        current_result = None

        while current1 is not None or current2 is not None or carry != 0:
            sum = carry
            if current1 is not None:
                sum += current1.value
                current1 = current1.next
            if current2 is not None:
                sum += current2.value
                current2 = current2.next

            carry = sum // 10
            new_node = Node(sum % 10)
            if result.head is None:
                result.head = new_node
            else:
                current_result.next = new_node
            current_result = new_node

        return result

    def printList(self):
        current = self.head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next

LinkedList([2,4,3]).addTwoNumbers(LinkedList([5,6,4])).printList()  # Output: 7