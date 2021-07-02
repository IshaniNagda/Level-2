class Solution:
    #Function to insert a node at the beginning of the linked list.
    def insertAtBegining(self,head,x):
        if head==None:
             newnode= Node(x)
             head=newnode
             newnode.next=None
            
        else:
            newnode= Node(x)
            newnode.next=head
            head=newnode
        
        return head
     
    
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        if head==None:
             newnode= Node(x)
             head=newnode
             newnode.next=None
        
        else:
            newnode= Node(x)
            newnode.next=None
            temp=head
            while(temp.next!=None):
                temp=temp.next
            temp.next=newnode
        
        return head
