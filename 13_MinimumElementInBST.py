def minValue(root):
    ##Your code here
    if root is None:
        return -1
    if root.left is None:
        return root.data
    else:
        current = root
        while current.left is not None:
            current = current.left
        
        return current.data
