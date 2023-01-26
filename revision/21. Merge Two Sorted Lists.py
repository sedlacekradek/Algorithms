def mergeTwoLists(list1, list2):
    list3 = ListNode()
    res = list3

    while list1 and list2:
        if list1.val <= list2.val:
            list3.next = list1
            list1 = list1.next
        else:
            list3.next = list2
            list2 = list2.next
        list3 = list3.next

    if list1:
        list3.next = list1
    if list2:
        list3.next = list2

    return res.next
