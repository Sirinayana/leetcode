class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        total=n*(n+1)//2
        missing_number=total-sum(nums)
        return missing_number
nums=[3,0,1]
solution=Solution()
print(solution.missingNumber(nums))
        