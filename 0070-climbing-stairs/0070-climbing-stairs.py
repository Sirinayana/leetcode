class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=2:
            return n
        first=1
        second=2
        for i in range(3,n+1):
            current=first+second
            first=second
            second=current
        return second
n=2
solution1=Solution()
print(solution1.climbStairs(n))

        