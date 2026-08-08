class Solution:
    def isPalindrome(self, x: int) -> bool:
        org=x
        rev=0
        while x>0:
            last=x%10
            rev=rev*10+last
            x=x//10
        return org==rev
        
        
solution1=Solution()
print(solution1.isPalindrome(121))


        