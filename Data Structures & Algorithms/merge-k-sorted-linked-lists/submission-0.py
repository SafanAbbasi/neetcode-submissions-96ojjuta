# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        k = len(lists)
        merged = lists[0]

        for idx in range(1,k):
            dummy = ListNode(0)
            l3 = dummy
            l1 , l2 = merged, lists[idx]

            while l1 and l2:
            
                if l1.val <= l2.val:
                    l3.next = l1
                    l1 = l1.next
                else:
                    l3.next = l2
                    l2 = l2.next

                l3 = l3.next

            if l1:
                l3.next = l1
            if l2:
                l3.next = l2
            
            merged = dummy.next

        return merged