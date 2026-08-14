class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in d:
                return [d[diff],i]
                break

            d[nums[i]]=i
            

nums=[2,7,11,15]
target=9
solution=Solution()
print(solution.twoSum(nums,target))


        