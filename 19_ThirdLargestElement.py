class Solution:
    def thirdLargest(self,a, n):
        max1=max2=max3=-1
        
        for i in range(n):
            if (a[i]>max1):
                max3=max2
                max2=max1
                max1=a[i]
            
            elif (a[i] > max2):
                max3=max2
                max2=a[i]
            
            elif(a[i] > max3):
                max3=a[i]
            
        
        
        return max3
