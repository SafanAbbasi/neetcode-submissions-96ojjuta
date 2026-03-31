# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head 
        curr = head
        prev = None 

        while curr:
            next_node = curr.next #
            curr.next = prev 

            prev = curr # move prev up one
            curr = next_node # move curr up one

        return prev
