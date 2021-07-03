def getNth(head, k):
    count=1
    temp=head
    while(temp.next!=None):
        if count==k:
            return temp.data
        else:
            count+=1
            temp=temp.next
    if count==k:
        return temp.data
    else:
        return -1
