class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        """
        ソートされた整数配列 nums と整数 n を指定されます。
        [1, n] の範囲内の任意の数値が配列内のいくつかの要素の合計で形成されるように、要素を配列に追加/パッチします。

        必要なパッチの最小数を返します。


        `miss` をこれまでカバーされていない最小の数とし、1で初期化する。
        配列 nums 要素を順番に見て、miss 以下なら miss に nums[i] を足す。
        これは、[1, miss) を使って、[1, miss + nums[i]) を作成することが可能なため
        nums[i] が miss より大きい場合、miss に miss を足す。
        これは、miss を配列に追加することで、miss と[1, miss) を使って、[1, miss + miss) を作成することが可能になるため。

        - Time complexity: O(n)
        - Space complexity: O(1)

        #Greedy

        Args:
            nums (list[int]): ソートされた整数配列
            n (int): 整数

        Returns:
            int: 必要なパッチの最小数を返します。
        """
        miss = 1
        ans = 0
        i = 0

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                ans += 1

        return ans


sol = Solution()
print(sol.minPatches(nums=[1, 3], n=6))
print(sol.minPatches(nums=[1, 5, 10], n=20))
print(sol.minPatches(nums=[1, 2, 2], n=5))
