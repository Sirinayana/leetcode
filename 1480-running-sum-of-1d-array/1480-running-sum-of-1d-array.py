class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total=0
        for i in range(len(nums)):
            total=total+nums[i]
            nums[i]=total
        return nums
nums=[1,2,3,4]
solution1=Solution()
print(solution1.runningSum(nums))
        