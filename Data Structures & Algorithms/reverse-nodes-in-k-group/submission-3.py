# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        d = ListNode(0, head)
        gpr = d
        while True:
            kth = self.getk(gpr, k)
            if not kth:
                break
            gnx = kth.next
            p, c = gnx, gpr.next
            while c != gnx:
                tmp = c.next
                c.next = p
                p = c
                c = tmp
            t = gpr.next
            gpr.next = kth
            gpr = t
        return d.next
    def getk(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr


        