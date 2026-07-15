class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse=0
        temp=x
        while x>0:
            digit=x%10
            reverse=reverse*10+digit
            x=x//10
        if reverse==temp:
            return True
        else:
            return False
x=121
solution1=Solution()
print(solution1.isPalindrome(x))
        