class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        n = len(nums1)
        m = len(nums2)

        ans = 0
        for i in range(n):
            for j in range(m):
                if nums1[i] % (nums2[j] * k) == 0:
                    ans += 1

        return ans


sol = Solution()
print(sol.numberOfPairs(nums1=[1, 3, 4], nums2=[1, 3, 4], k=1))
print(sol.numberOfPairs(nums1=[1, 2, 4, 12], nums2=[2, 4], k=3))
