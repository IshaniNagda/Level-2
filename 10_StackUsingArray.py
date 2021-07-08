class MyStack:
    
    def __init__(self):
        self.arr=[]
    
    #Function to push an integer into the stack.
    def push(self,data):
        self.arr.append(data)

    #Function to remove an item from top of the stack.
    def pop(self):
        if (len(self.arr)!=0):
            lastelement= self.arr[-1]
            del(self.arr[-1])
            return lastelement
        else:
            return -1
