def reverseList(head):

    def reverse(current, prev):
        if current is None:
            return prev
        else:
            next = current.next
            current.next = prev
            reverse(current = next, prev=current)

    return reverse(head, prev=None)