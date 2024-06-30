class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        """
        整数配列 nums と正の整数 k が与えられます。
        長さが x の nums の部分列 sub は、次の条件を満たす場合に有効と呼ばれます。

        - (sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) %k

        nums の最長の有効な部分列の長さを返します。

        - Time complexity: O(n * k)
        - Space complexity: O(k)

        #DP

        Args:
            nums (list[int]): 整数配列
            k (int): 正の整数

        Returns:
            int: nums の最長の有効な部分列の長さを返します。
        """
        n = len(nums)
        # print(f"nums={nums}")

        ans = 0

        for v in range(0, k):
            dp: list[int] = [0] * k
            # print(f"v={v}")

            for n in nums:
                # print(f"n%k={n%k}, (v-n)%k={(v-n)%k}")
                dp[n % k] = max(dp[n % k], dp[(v - n) % k] + 1)
                # print(f"dp={dp}")
            ans = max(ans, max(dp))

        return ans


sol = Solution()
print(sol.maximumLength(nums=[1, 2, 3, 4, 5], k=2))
print(sol.maximumLength(nums=[1, 4, 2, 3, 1, 4], k=3))
print(sol.maximumLength(nums=[3, 6, 3, 6], k=5))  # 4
print(sol.maximumLength(nums=[3, 6, 3, 3], k=5))  # 3
print(sol.maximumLength(nums=[1, 2, 3, 10, 2], k=6))  # 3
