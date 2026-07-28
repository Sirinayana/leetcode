class Solution:
    def containsDuplicate(self, nums):
        d={}
        for num in nums:
            if num in d:
                return True
            d[num]=1
        return False
nums = [1,2,3,4]
solution = Solution()
print(solution.containsDuplicate(nums))


        