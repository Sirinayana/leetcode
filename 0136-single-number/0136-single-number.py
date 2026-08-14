class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for key,value in d.items():
            if value==1:
                return key
nums=[2,2,1]
solution1=Solution()
print(solution1.singleNumber(nums))


        