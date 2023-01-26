"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
"""

def reverseList(head):
    # O (n)
    # 1 -> 2 -> 3 -> None
    # 3 -> 2 -> 1-> None
    current = head  # 1
    prev = None

    while current:
        next = current.next  # save variable so that we can recall it after current.next is changed
        current.next = prev  # reverse the order for current.next
        prev = current  # update prev variable
        current = next  # move one node to the right
    return prev  # return new head