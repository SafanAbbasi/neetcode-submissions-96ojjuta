# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        res = ListNode(0)      # dummy head for result list
        cur = res              # pointer to build the result
        minHeap = []
        counter = 0

        # push all list heads into heap
        for l in lists:
            if l:
                heapq.heappush(minHeap, (l.val, counter, l))
                counter += 1

        # Main loop — pop smallest, push its next:
        while minHeap:
            val, _, node = heapq.heappop(minHeap)  # get smallest
            cur.next = node                         # attach to result
            cur = cur.next                          # advance result pointer

            if node.next:                           # if that list has more nodes
                heapq.heappush(minHeap, (node.next.val, counter, node.next))
                counter += 1

        return res.next