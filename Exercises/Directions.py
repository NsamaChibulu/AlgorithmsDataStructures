
# definition of binary tree node

# class TreeNode(object):
#     def __int__(self, val=0, left=None, right=None, parent=1):
#         self.val = val
#         self.left = left
#         self.right = right 
#         self.parent = parent

from pip import List, Optional



class Solution:
    def getDirections(self, root, startValue: int, destValue: int) -> str:
        def find(n, val: int, path: List[str]) -> bool:
            if n.val == val:
                return True
            if n.left and find(n.left, val, path):
                path += "L"
            elif n.right and find(n.right, val, path):
                path += "R"
            return path
        s, d = [], [] # create empty arrays to populate with position node
        find(root, startValue, s)
        find(root, destValue, d)

        while len(s) and len(d) and s[-1] == d[-1]:
            s.pop()
            d.pop()
        return "".join("U" * len(s)) + "".join(reversed(d))            

        
    

        