class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        while n%3==0:
            n//=3
        return n==1
n=27
solution1=Solution()
print(solution1.isPowerOfThree(n))
        