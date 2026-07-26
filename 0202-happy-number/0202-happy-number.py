class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!=0 and n not in seen:
            seen.add(n)
            sum=0
            while n!=0:
                last=n%10
                sum+=last*last
                n=n//10
            n=sum
        return n==1
n=19
solution1=Solution()
print(solution1.isHappy(n))
        