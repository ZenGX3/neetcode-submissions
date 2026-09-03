"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = {None : None}
        cur = head
        while cur:
            cpy = Node(cur.val)
            d[cur] = cpy
            cur = cur.next
        cur = head
        while cur:
            cpy = d[cur]
            cpy.next = d[cur.next]
            cpy.random = d[cur.random] 
            cur = cur.next
        
        return d[head]
