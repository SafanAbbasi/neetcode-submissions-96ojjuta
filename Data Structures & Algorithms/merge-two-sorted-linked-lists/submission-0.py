# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None) # create dummy node 
        list3 = dummy

        if not list1:
            return list2
        if not list2:
            return list1

        while list1 and list2:
            if list1.val <= list2.val:
                list3.next = list1
                list1 = list1.next 
            else:
                list3.next = list2
                list2 = list2.next

            list3 = list3.next # have to move it forward

        if list1:
            list3.next = list1
        elif list2:
            list3.next = list2

        return dummy.next





