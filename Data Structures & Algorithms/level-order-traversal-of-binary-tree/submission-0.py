# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        l = []
        q.append(root)
        while q:
            ql = len(q)
            lv = []
            for i in range(ql):
                n = q.popleft()
                if n:
                    lv.append(n.val)
                    q.append(n.left)
                    q.append(n.right)
            if lv:
                l.append(lv)
        return l

