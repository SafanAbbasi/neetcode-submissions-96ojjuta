# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # if you have a reverse linked list and a forward linked list 
        # then you can interleave them
        # do I need to create a new list to do that
        
        start = head
        slow = head
        fast = head
        tail = None
        while fast and fast.next:
            tail = slow
            slow = slow.next
            fast = fast.next.next

        # now slow in in the midpoint
        # tail is right before slow
        if not head.next:
            return
        tail.next = None  # <-- here, sever the first half

        ### revesee 2nd half


        currslow = slow
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev

            prev = slow
            slow = next_node


        # [1,2]  # start is head of orignial list
        # [5,4,3] head of this list is prev
        dummy = ListNode(0)
        tail = dummy
        while start and prev:
            start_next_node = start.next
            prev_next_node = prev.next

            tail.next = start
            tail.next.next = prev

            tail = tail.next.next

            start = start_next_node
            prev = prev_next_node
            
        if start:
            tail.next = start
        if prev:
            tail.next = prev
