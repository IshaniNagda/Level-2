class Solution:
    
    #Function to count nodes of a linked list.
    def getCount(self, head_node):
        count=0
        temp=head_node
        while(temp.next!=None):
            count+=1
            temp=temp.next
        return count+1
