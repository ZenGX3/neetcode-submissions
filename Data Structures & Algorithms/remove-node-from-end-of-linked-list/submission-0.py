# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nxt = head
        p = head
        q = head
        c = 0
        while p:
            c += 1
            p = p.next
        ind = c-n
        if ind == 0:
            return head.next
        for i in range(ind-1):
            q = q.next
        q.next = q.next.next
        return head
        