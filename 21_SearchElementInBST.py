class BST:
    
    #Function to search a node in BST.
    def search(self, node, x):
        #code here
        if node== None:
            return 0
        if x== node.data:
            return 1
        
        if x<node.data:
            return self.search(node.left, x)
        
        elif x>node.data:
            return self.search(node.right, x)
