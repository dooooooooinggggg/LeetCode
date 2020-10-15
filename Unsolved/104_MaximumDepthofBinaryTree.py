# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # def maxDepth(self, root: TreeNode) -> int:
    def maxDepth(self, root: TreeNode):
        if (root == None):
            return 0

        dep = 1

        aiueo = [0]
        if (root.left != None):
            aiueo.append(self.find_left(dep+1, root.left))

        if(root.right != None):
            aiueo.append(self.find_right(dep+1, root.right))

        print(aiueo)
        print(dep)

        if max(aiueo) > dep:
            return max(aiueo)
        else:
            return dep

    def find_left(self, dep, tmp):
        if (tmp.left != None):
            self.find_left(dep+1, tmp.left)

        if(tmp.right != None):
            self.find_right(dep+1, tmp.right)

        return dep

    def find_right(self, dep, tmp):
        if (tmp.left != None):
            self.find_left(dep+1, tmp.left)

        if(tmp.right != None):
            self.find_right(dep+1, tmp.right)

        return dep
