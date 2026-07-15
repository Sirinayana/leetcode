class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            sum=0
            while num>0:
                last=num%10
                sum=sum+last
                num=num//10
            num=sum
        return num
num=38
solution1=Solution()
print(solution1.addDigits(num))

        