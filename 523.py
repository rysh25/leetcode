class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        """
        整数配列 nums と整数 k が与えられた場合、nums に適切なサブ配列がある場合は true を返し、そうでない場合は false を返します。

        適切なサブ配列とは、次の条件を満たすサブ配列です:

        - 長さが少なくとも 2 であり、
        - サブ配列の要素の合計が k の倍数である。


        [i, j) の合計あまりはは、(prefix_sum[j] % k) - (prefix_sum[i] % k) となる
        プレフィックスサムを計算し、そのあまりの数を数えることで、あまりが同じ場合、あまりが0となる。
        ただし、j-i=1 の場合は、長さが1のため、長さが少なくとも2の条件を満たさない。

        - Time complexity: O(n)
        - Space complexity: O(n)

        #Math
        #PrefixSum

        Args:
            nums (list[int]): 整数配列
            k (int): 整数

        Returns:
            bool: nums に適切なサブ配列がある場合は true を返し、そうでない場合は false を返します。
        """
        from collections import defaultdict

        n = len(nums)
        remainder: defaultdict[int, int] = defaultdict(int)

        last_r = 0
        prefix_sum = 0
        remainder[0] += 1  # あまり0

        for i in range(n):
            prefix_sum += nums[i]
            r = prefix_sum % k
            if last_r != r and remainder[r] > 0:
                return True
            elif last_r == r and remainder[r] > 1:
                return True
            remainder[r] += 1
            last_r = r

        print(f"remainder={remainder}")

        return False


sol = Solution()
print(sol.checkSubarraySum(nums=[23, 2, 4, 6, 7], k=6))
print(sol.checkSubarraySum(nums=[23, 2, 6, 4, 7], k=6))
print(sol.checkSubarraySum(nums=[23, 2, 6, 4, 7], k=13))
print(sol.checkSubarraySum(nums=[23, 2, 4, 6, 6], k=7))
print(sol.checkSubarraySum(nums=[5, 0, 0, 0], k=3))
