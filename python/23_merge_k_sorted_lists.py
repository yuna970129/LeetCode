# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
            if lists[i] != None:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        root = current = ListNode(0)
        while heap:
            v, idx, ln = heapq.heappop(heap)
            current.next = ListNode(v)
            current = current.next
            if ln.next != None:
                heapq.heappush(heap, (ln.next.val, idx, ln.next))
        return root.next
