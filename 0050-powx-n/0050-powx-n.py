class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans=1.0
        temp=n
        if n<0: temp=-1*n
        while(temp):
            if temp%2==1:
                ans=ans*x
                temp=temp-1
            elif temp%2==0:
                x=x*x
                temp=temp//2
        if n <0:
            return 1/ans
        else:
            return ans
 