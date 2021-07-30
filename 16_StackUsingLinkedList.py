class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class MyStack:
    def __init__(self):
        self.front=None
        self.rear=None

    #Function to push an integer into the stack.
    def push(self, data):
        temp= Node(data)
        if self.front is None:
            self.front= self.rear=temp
        
        else:
            temp.next=self.front
            self.front=temp
        
        

    #Function to remove an item from top of the stack.
    def pop(self):
        if self.front is None:
            return -1
        val= self.front.data
        self.front= self.front.next
        return val
