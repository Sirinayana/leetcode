class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d={}
        for i in magazine:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in ransomNote:
            if i  not in d :
                return False
            d[i]-=1
            if d[i]<0:
                return False
        return True
ransomNote = "a"
magazine = "b"
solution1=Solution()
print(solution1.canConstruct(ransomNote,magazine))

        