class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        max_num=float("-inf")
        for i in range(0,len(nums)):
            sum+=nums[i]
            if sum>max_num:
                max_num=sum
            if sum <0:
                sum=0
        return max_num  
nums = [-2,1,-3,4,-1,2,1,-5,4]
solution1=Solution()
print(solution1.maxSubArray(nums))      