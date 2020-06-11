# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # def searchBST(self, root: TreeNode, val: int) -> TreeNode:
    def searchBST(self, root: TreeNode, val: int):

        tmp_root = root
        while(1):
            if val == tmp_root.val:
                return tmp_root
            elif val < tmp_root.val:
                tmp_root = tmp_root.left
            elif val > tmp_root.val:
                tmp_root = tmp_root.right

            if tmp_root == None:
                return tmp_root
