# Definition of binary tree
# class TreeNode(object):
#     def __init__(self, val=0, left=0, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 



import collections


class Solution(object):
    def findLeaves(self, root):
        def order(root, dic):
            if not root:
                return 0
            left = order(root.left, dic)
            right = order (root.right, dic)
            lev = max(left, right) + 1
            dic[lev] += root.val,
            return lev
        dic, ret = collections.defaultdict(list), []
        order(root,dic)
        for i in range (1, len(dic) + 1):
            ret.append(dic[i])
        return ret 