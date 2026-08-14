class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        total=n*(n+1)//2
        missing=total-sum(nums)
        return missing
nums=[3,0,1]
solution=Solution()
print(solution.missingNumber(nums))
        