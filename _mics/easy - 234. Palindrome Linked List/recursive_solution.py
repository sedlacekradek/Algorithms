# times out on leetcode, better solution would be to reverse second half of the list and compare vals
# should be give correct though, just the time complexity is O(through the roof)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    def recur(head):
        first = head
        while head.next and head.next.val != None:
            head = head.next
        if first.val != head.val:
            return False
        head.val = None
        if first.next and first.next.val != None:
            return recur(head=first.next)
        else:
            return True

    return recur(head)


one = ListNode(1)
two = ListNode(2)
three = ListNode(2)
four = ListNode(1)

one.next = two
two.next = three
three.next = four

print(isPalindrome(one))
