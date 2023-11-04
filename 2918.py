class Solution:
    def minSum(self, nums1: list[int], nums2: list[int]) -> int:
        sum1 = sum(nums1)
        count1 = nums1.count(0)
        sum2 = sum(nums2)
        count2 = nums2.count(0)

        # print(f"nums1={nums1}, sum1={sum1}, count1={count1}")
        # print(f"nums2={nums2}, sum2={sum2}, count2={count2}")

        if sum1 + count1 > sum2 + count2:
            return self.minSum(nums2, nums1)

        target = sum2 + count2
        # print(f"target={target}")

        if sum1 + count1 > target:
            # print("-1: 1")
            return -1
        if target - sum1 > 0 and count1 == 0:
            # print("-1: 2")
            return -1

        return target


sol = Solution()
print(sol.minSum(nums1=[3, 2, 0, 1, 0], nums2=[6, 5, 0]))
print(sol.minSum(nums1=[2, 0, 2, 0], nums2=[1, 4]))
print(sol.minSum(nums1=[1, 4], nums2=[1, 4, 0]))
print(
    sol.minSum(
        nums1=[8, 13, 15, 18, 0, 18, 0, 0, 5, 20, 12, 27, 3, 14, 22, 0],
        nums2=[29, 1, 6, 0, 10, 24, 27, 17, 14, 13, 2, 19, 2, 11],
    )
)  # 179
