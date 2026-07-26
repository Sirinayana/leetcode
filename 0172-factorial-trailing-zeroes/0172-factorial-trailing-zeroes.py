class Solution:
    def trailingZeroes(self, n: int) -> int:
        count=0
        while n > 0:
            n //= 5
            count += n

        return count
n=3
solution1=Solution()
print(solution1.trailingZeroes(n))
        