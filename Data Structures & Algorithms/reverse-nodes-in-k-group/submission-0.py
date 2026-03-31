# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = head
        dummy = ListNode()
        prev_tail = dummy
        
        while start:
            group_end = None
            count = 0
            curr = start
            while count < k and curr:
                group_end = curr
                curr = curr.next
                count += 1
            if count == k:
                group_end.next = None     # sever at the actual end
                newhead = self.reverse(start) # beginnging of first k nodes
                prev_tail.next = newhead
                prev_tail = start
                start.next = curr
                start = curr

            else: 
                prev_tail.next = start
                break

        return dummy.next



    def reverse(self, listnode : Optional[ListNode]):

        curr = listnode
        prev = None
        while curr:
            curr_next = curr.next
            curr.next = prev 

            prev = curr
            curr = curr_next


        return prev