class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue:
    
    def __init__(self):
        self.front= None
        self.rear= None
        
    def isEmpty(self):
        return self.front==None
        
    
    #Function to push an element into the queue.
    def push(self, item): 
        temp= Node(item)
        if self.front==None:
            self.front= self.rear=temp
        
        else:
            self.rear.next=temp
            self.rear=temp
