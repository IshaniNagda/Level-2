class Solution: 
    
    
    def deleteAlt(self, head):
        temp=head
        while(temp.next!=None and temp!=None):
            if temp.next.next==None:
                temp.next=None
                break
                
            temp.next= temp.next.next
            temp=temp.next
        
        return head
