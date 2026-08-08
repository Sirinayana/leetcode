class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for key,value in d.items():
            if value==1:
                return s.index(key)
                break
        else:
            return -1
s="leetcode"
solution1=Solution()
print(solution1.firstUniqChar(s))

        