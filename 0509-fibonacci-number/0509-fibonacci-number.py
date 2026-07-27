class Solution:
    def fib(self, n: int) -> int:
        if n <2:
            return n
        first=0
        second=1
        for i in range(2,n+1):
            current=first+second
            first=second
            second=current
        return second
n=2
solution1=Solution()
print(solution1.fib(n))


        