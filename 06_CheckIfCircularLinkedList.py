def isCircular(head):
    temp=head
    while(temp.next!=head and temp.next!=None):
        temp=temp.next
    
    if temp.next==head:
        return 1
    elif temp.next==None:
        return False
