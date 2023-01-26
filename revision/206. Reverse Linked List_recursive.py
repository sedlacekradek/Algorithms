def solution(head):

    prev = None

    def reverse(current, prev):
        if current is None:
            return prev

        next = current.next
        current.next = prev
        prev = current
        return reverse(next, current)

    return reverse(head, prev)

