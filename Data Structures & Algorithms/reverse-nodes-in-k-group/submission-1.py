
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
         
        # need to figure out if there are k nodes left
        # know the start and end of the portion to reverse
        # continue forward
        # can have a helper do the reversing

        dummy = ListNode()
        prev_tail = dummy
        start = head

        while start:
            
            count = 0

            curr = start
            tail = curr
            while count < k and curr: 
                tail = curr
                curr = curr.next
                count += 1
            
            # curr is at the next portion of nodes

            if count == k:
                # sever the first set of nodes
                tail.next = None
                
                # return 3. this is the new beginnign of the list
                newhead = self.reversek(start)

                prev_tail.next = newhead

                prev_tail = start

                
                # start of next k nodes
                start.next = curr # link starts next to curr

                start = curr
                
            else: 
                prev_tail.next = start
                break

        return dummy.next



    def reversek(self, klist : Optional[ListNode]):
        
        prev = None
        curr = klist

        while curr:

            curr_next = curr.next
            curr.next = prev

            prev = curr
            curr = curr_next
        
        return prev
