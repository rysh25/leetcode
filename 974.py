class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        """
        整数配列 nums と整数 k が渡されます。
        合計が k で割り切れる空でない部分配列の数を返します。


        [i, j) の合計あまりはは、(prefix_sum[j] % k) - (prefix_sum[i] % k) となる。
        前から順に prefix sum を計算し、それまでに同じあまりの prefix sum が何回あったかが、そこまでの合計が k で割り切れる部分配列の数となる。
        prefix sum が0の場合、それまでのすべて要素を利用した部分配列が割り切れると数えるためあらかじめあまり0を1カウントしておく。

        - Time complexity: O(n)
        - Space complexity: O(n)

        #Math
        #PrefixSum

        Args:
            nums (list[int]): 整数配列
            k (int): と整数

        Returns:
            int: 合計が k で割り切れる空でない部分配列の数を返します。
        """

        counts: list[int] = [0] * k
        n = len(nums)
        prefix_sum = 0
        counts[0] += 1
        count = 0

        for i in range(n):
            prefix_sum = (prefix_sum + nums[i] % k + k) % k
            count += counts[prefix_sum]
            counts[prefix_sum] += 1

        # print(f"count={counts}")
        return count


sol = Solution()
print(sol.subarraysDivByK(nums=[4, 5, 0, -2, -3, 1], k=5))
print(sol.subarraysDivByK(nums=[5], k=9))
