class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        """
        nums1 と nums2 の2つの配列が渡される。
        nums1 と nums2 の空でない部分列の内積の最大を返す。

        #DP

        Args:
            nums1 (List[int]): 配列が渡される。
            nums2 (List[int]): 配列が渡される。

        Returns:
            int: nums1 と nums2 の空でない部分列の内積の最大を返す。
        """
        # print(f"nums1={nums1}, nums2={nums2}, n={n}")

        INF = 10**9 + 1

        dp: list[list[int]] = [[-INF] * 505 for _ in range(505)]
        dp[0][0] = 0

        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                dp[i][j] = max(
                    nums1[i - 1] * nums2[j - 1],
                    dp[i - 1][j - 1] + nums1[i - 1] * nums2[j - 1],
                    dp[i - 1][j],
                    dp[i][j - 1],
                )
        return dp[len(nums1)][len(nums2)]


sol = Solution()
print(sol.maxDotProduct(nums1=[2, 1, -2, 5], nums2=[3, 0, -6]))
print(sol.maxDotProduct(nums1=[3, -2], nums2=[2, -6, 7]))
print(sol.maxDotProduct(nums1=[-1, -1], nums2=[1, 1]))
print(sol.maxDotProduct(nums1=[5, -4, -3], nums2=[-4, -3, 0, -4, 2]))  # 28
