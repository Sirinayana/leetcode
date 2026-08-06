class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = {}

        # Count characters in s
        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1

        # Subtract characters of t
        for ch in t:
            if ch not in d:
                return ch

            d[ch] -= 1

            if d[ch] < 0:
                return ch

        return ""
                
s="abcd"
t="abcde"
solution1=Solution()
print(solution1.findTheDifference(s,t))
        