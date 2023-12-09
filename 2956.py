class Solution:
    def findIntersectionValues(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans: list[int] = [0, 0]

        for i in nums1:
            if i in nums2:
                ans[0] += 1

        for i in nums2:
            if i in nums1:
                ans[1] += 1

        return ans


sol = Solution()
print(sol.findIntersectionValues(nums1=[4, 3, 2, 3, 1], nums2=[2, 2, 5, 2, 3, 6]))
print(sol.findIntersectionValues(nums1=[3, 4, 2, 3], nums2=[1, 5]))
