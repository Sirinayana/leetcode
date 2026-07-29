class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        n = len(nums)
        for key, value in freq.items():
            if value > n // 2:
                return key
nums=[2,2,1,1,1,2,2]
solution=Solution()
print(solution.majorityElement(nums))
        
        