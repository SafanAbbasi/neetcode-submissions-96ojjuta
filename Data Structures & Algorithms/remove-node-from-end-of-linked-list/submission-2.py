# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # should I get the lenght of the list in the first pass and then do a second pass to remove it

        # find length

        length = 0

        start = head

        while start:
            length += 1
            start = start.next

        # item to remove is  at index (length - n)
        index = length - n

        start = head
        prev = None
        while index >= 0:

            if index == 0:
                if prev:
                    prev.next = start.next
                    break
                else:
                    head = start.next

            start_next_node = start.next              
            prev = start
            start = start_next_node

            index -= 1

        return head
        # now start is at idx



        # for the last while loop can do the below instead

        # dummy = ListNode(0, head)
        # start = dummy
        # index = length - n

        # while index > 0:
        #     start = start.next
        #     index -= 1

        # start.next = start.next.next
        # return dummy.next
