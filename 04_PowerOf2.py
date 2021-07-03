def isPowerofTwo(self,n):
        if n<1:
            return False
        while n%2==0:
            n=n/2
        if n==1:
            return True
        else:
            return False
