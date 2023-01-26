"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



# Time Complexity: O(n+m)
def mergeTwoLists(list1, list2):
    # create a new linked list that we will return
    dummy = ListNode()
    # create a "pointer" - pointing to a current dummy node; we do not want to use dummy as a pointer
    # because at the end we need to return the dummy.head (which will actually be dummy.next because it initializes
    # with head of 0 as the starting value)
    tail = dummy

    # comparing list1 and list2 values and adding the lower value
    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    # loop will stop once one of the lists runs out of values but there could still be values in the other list
    # if the lists have different numbers of nodes
    # the easiest way to append the remaining nodes is as follows:
    if list1:
        tail.next = list1
    if list2:
        tail.next = list2

    # return the head of our new list
    return dummy.next