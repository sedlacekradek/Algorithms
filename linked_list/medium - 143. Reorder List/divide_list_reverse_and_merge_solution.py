"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
"""


def reorderList(head) -> None:
    """
    Do not return anything, modify head in-place instead.
    """

        # find second half
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # set beginning of first and second half
        first = head
        second = slow.next

        # new ending of list
        slow.next = None

        # reverse second half
        prev = None
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next
        # when loop ends, prev will be the beginning of our second half of the list

        second = prev
        while second:
            temp_first = first.next
            temp_second = second.next
            first.next = second
            second.next = temp_first
            first = temp_first
            second = temp_second