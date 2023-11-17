class Solution:
    def minOperations(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        prefix_max1: list[int] = [nums1[0]] * n
        prefix_max2: list[int] = [nums2[0]] * n
        for i in range(1, n):
            prefix_max1[i] = max(prefix_max1[i - 1], nums1[i])
            prefix_max2[i] = max(prefix_max2[i - 1], nums2[i])

        # print(f"prefix_max1={prefix_max1}")
        # print(f"prefix_sum2={prefix_max2}")

        max1 = max(nums1)
        max2 = max(nums2)
        if nums1[-1] == max1 and nums2[-1] == max2:
            return 0

        count = 0
        for i in range(n):
            if nums1[i] < nums2[i]:
                count += 1
                nums2[i], nums1[i] = nums1[i], nums2[i]
                prefix_max1[i] = max(prefix_max1[i - 1], nums1[i])
                prefix_max2[i] = max(prefix_max2[i - 1], nums2[i])

        max1 = max(nums1)
        max2 = max(nums2)

        if nums1[-1] != max1 or nums2[-1] != max2:
            return -1

        # print(f"count={count}")
        ans = n - count if n - count < count else count
        return ans


sol = Solution()
# print(sol.minOperations(nums1=[1, 2, 7], nums2=[4, 5, 3]))
# print(sol.minOperations(nums1=[2, 3, 4, 5, 9], nums2=[8, 8, 4, 4, 4]))
# print(sol.minOperations(nums1=[1, 5, 4], nums2=[2, 5, 3]))
# print(sol.minOperations(nums1=[1, 4, 16], nums2=[16, 16, 16]))
# print(sol.minOperations(nums1=[1, 2, 7], nums2=[4, 5, 3]))  # 1
print(sol.minOperations(nums1=[8, 6, 6, 6, 7, 8], nums2=[5, 8, 8, 8, 7, 7]))  # 2
