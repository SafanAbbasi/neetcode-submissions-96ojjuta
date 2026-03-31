# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # fast and slow pointer approach. Fast will always catch back up with slow if there is a cycle

        slow = head
        if head and head.next:
            fast = head.next
        else:
            fast = head
        while fast and fast.next:
            if slow == fast:
                return True 

            slow = slow.next
            fast = fast.next.next

        return False