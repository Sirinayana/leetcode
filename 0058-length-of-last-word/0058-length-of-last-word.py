class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1=s[::-1].strip()
        count=0
        for i in range(len(s1)):
            if s1[i]!=" ":
                count+=1
            else:
                break
        return count
s="Hello World"
solution1=Solution()
print(solution1.lengthOfLastWord(s))
        