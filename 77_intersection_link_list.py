def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None

    # Compute lengths
    def getLength(head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    lenA, lenB = getLength(headA), getLength(headB)

    # Align the longer list
    while lenA > lenB:
        headA = headA.next
        lenA -= 1
    while lenB > lenA:
        headB = headB.next
        lenB -= 1

    # Walk together
    while headA and headB:
        if headA == headB:
            return headA
        headA, headB = headA.next, headB.next

    return None

def getIntersectionNode2(headA, headB):
    if not headA or not headB:
        return None

    currentA, currentB = headA, headB
    while currentA != currentB:
        currentA = currentA.next if currentA else headB
        currentB = currentB.next if currentB else headA

    return currentA
