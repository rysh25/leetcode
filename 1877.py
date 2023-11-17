class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        """
        あるペア (a,b) のペア和は a + b と等しい。最大ペアの和は、ペアのリストの中で最も大きいペアの和である。

        偶数長の配列 nums が与えられたとき、次のようにして nums の要素を n / 2 のペアに組み合わせる。

        - nums の各要素はちょうど一つのペアに含まれること。
        - 最大ペア和が最小化されること。

        要素を最適にペアリングした後の最小化された最大ペア和を返す。


        配列をソートし、その i 番目の要素と、n-i番目の要素を足したものの最大値を求める。
        その値が、ペアの最大値の最小化となる。

        - Time complexity: O(n log n)
        - Time complexity: O(n)

        Args:
            nums (list[int]): 偶数長の配列

        Returns:
            int: 要素を最適にペアリングした後の最小化された最大ペア和を返す。
        """
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n // 2):
            ans = max(ans, nums[i] + nums[n - i - 1])

        return ans


sol = Solution()
print(sol.minPairSum(nums=[3, 5, 2, 3]))
print(sol.minPairSum(nums=[3, 5, 4, 2, 4, 6]))
