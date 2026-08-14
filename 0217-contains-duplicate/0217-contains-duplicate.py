class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d={}
        for i in nums:
            if i in d:
                return True
            d[i]=1
        
        return False
nums=[1,2,3,1]
solution=Solution()
print(solution.containsDuplicate(nums))
        