def insertInMid(head,node):
    if head==None:
        head=node
        return head
    else:
        slow=head
        fast=head.next
   
        while(slow.next!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next
            if fast.next:
                fast=fast.next
            
    
        node.next=slow.next
        slow.next=node
        return head
