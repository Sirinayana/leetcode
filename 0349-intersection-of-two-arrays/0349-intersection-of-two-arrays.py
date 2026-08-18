class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen=set(nums1)
        res=set()
        for x in nums2:
            if x in seen:
                res.add(x)
        return list(res)
        
nums1=[1,2,2,1]
nums2=[2,2]
solution1=Solution()
print(solution1.intersection(nums1,nums2))



        