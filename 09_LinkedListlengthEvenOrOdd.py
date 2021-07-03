def isLengthEvenOrOdd(head):
    count=0
    temp=head
    while(temp!=None):
        count+=1
        temp=temp.next
    
    return not(count%2)
