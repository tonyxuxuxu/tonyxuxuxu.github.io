class Solution:
    def buildtree(self, preorder, inorder):
        if inorder:
            root_index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[root_index])
            root.left = self.buildtree(preorder, inorder[:root_index])
            rootright = self.buildtree(preorder, inorder[root_index+1:])
            return root
