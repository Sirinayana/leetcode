class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in t:
            if i not in d:
                return False
            d[i]=d[i]-1
        if d[i]<0:
            return False
        for value in d.values():
            if value!=0:
                return False
        return True
s="anagram"
t="nagaram"
solution1=Solution()
print(solution1.isAnagram(s,t))
        
        