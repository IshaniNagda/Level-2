def areIdentical(head1, head2):
    l1=[]
    l2=[]
    temp1=head1
    temp2=head2
    while(temp1!=None):
        l1.append(temp1.data)
        temp1=temp1.next
    
    while(temp2!=None):
        l2.append(temp2.data)
        temp2=temp2.next
    
    if l1==l2:
        return True
    else:
        return False
