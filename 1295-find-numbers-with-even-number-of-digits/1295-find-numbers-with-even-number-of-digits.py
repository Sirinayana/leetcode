class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            a=str(i)
            if len(a)%2==0:
                count+=1
        return count
nums=[12,345,2,6,7896]
solution=Solution()
print(solution.findNumbers(nums))

        