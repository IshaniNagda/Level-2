class Solution:
    #Function to find triplets with zero sum.    
    def findTriplets(self, arr, n):
        if n<3:
            return 0
        
        arr.sort()
        for i in range(0,n-2):
            j=i+1
            k=n-1
            while(j<k):
                add= arr[i]+arr[j]+arr[k]
                    
                if add==0: return 1
                elif add>0: k-=1
                elif add<0: j+=1
            
        return 0
