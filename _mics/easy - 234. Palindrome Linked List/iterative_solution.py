# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res_list = []
        while head:
            res_list.append(head.val)
            head = head.next

        l = 0
        r = len(res_list) - 1
        while l < r:
            if res_list[l] != res_list[r]:
                return False
            l += 1
            r -= 1

        return True