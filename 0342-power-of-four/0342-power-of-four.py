class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <=0:
            return False
        while n%4==0:
            n=n//4
        return n==1
n=16
solution1=Solution()
print(solution1.isPowerOfFour(n))
        