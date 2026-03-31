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

        while fast.next and fast.next.next:
            
            slow = slow.next
            fast = fast.next.next
        
        # slow = 3, fast = 6

        second = slow.next # 4

        # sever first half
        slow.next = None 
        # reverse 2nd half 
        prev = None
        while second:
            second_next_node = second.next
            second.next = prev
        
            prev = second
            second = second_next_node

        # [0,1,2,3]
        # [6,5,4]

        # interleave

        while prev:
            start_next_node = start.next
            prev_next_node = prev.next

            start.next = prev
            prev.next = start_next_node

            prev = prev_next_node
            start = start_next_node
        