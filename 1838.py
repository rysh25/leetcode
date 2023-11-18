class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        """
        要素の頻度は、配列内でその要素が出現する回数です。

        整数配列 nums と整数 k が与えられます。
        1 回の操作で、nums のインデックスを選択し、
        そのインデックスの要素を 1 ずつ増やすことができます。

        最大 k 個の操作を実行した後、要素の可能な最大頻度を返します。

        Args:
            nums (list[int]): 整数配列
            k (int): 整数

        Returns:
            int: 最大 k 個の操作を実行した後、要素の可能な最大頻度を返します。
        """
        # print(f"nums={nums}, k={k}")
        n = len(nums)
        nums.sort()

        l = 0
        curr = 0
        ans = 0
        for r in range(n):
            curr += nums[r]

            while (r - l + 1) * nums[r] - curr > k:
                curr -= nums[l]
                l += 1
            ans = max(ans, r - l + 1)

        return ans


sol = Solution()
print(sol.maxFrequency(nums=[1, 2, 4], k=5))
print(sol.maxFrequency(nums=[1, 4, 8, 13], k=5))
print(sol.maxFrequency(nums=[3, 9, 6], k=2))
print(
    sol.maxFrequency(
        nums=[
            9940,
            9995,
            9944,
            9937,
            9941,
            9952,
            9907,
            9952,
            9987,
            9964,
            9940,
            9914,
            9941,
            9933,
            9912,
            9934,
            9980,
            9907,
            9980,
            9944,
            9910,
            9997,
        ],
        k=7925,
    )  # 22
)
