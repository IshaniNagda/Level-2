class Solution:
    def InOrder(self,root):
        inorder=[]
        self.inOrderTraversal(root,inorder)
        return inorder

    def inOrderTraversal(self,root,inorder):
        if root:
            self.inOrderTraversal(root.left,inorder)
            inorder.append(root.data)
            self.inOrderTraversal(root.right,inorder)
