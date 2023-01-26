def solution(head):
    prev = None

    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next

    return prev
