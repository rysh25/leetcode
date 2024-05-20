class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        """
        配列の XOR 合計は、そのすべての要素のビット単位の XOR として定義され、配列が空の場合は 0 として定義されます。

        配列 nums が渡されます。
        nums のすべてのサブセットのすべての XOR 合計の合計を返します。


        Bit 全探索を行う。

        - Time complexity: O(2^n)
        - Space complexity: O(n)

        #BruteForce
        #BitManipulaiton
        #Combinatorics

        Args:
            nums (list[int]): 配列

        Returns:
            int: nums のすべてのサブセットのすべての XOR 合計の合計を返します。
        """
        n = len(nums)

        ans = 0
        for bit in range(0, 1 << n):
            xor = 0
            for i in range(n):
                if (bit >> i) & 1 == 1:
                    xor ^= nums[i]

            ans += xor

        return ans


sol = Solution()
print(sol.subsetXORSum(nums=[1, 3]))
print(sol.subsetXORSum(nums=[5, 1, 6]))
print(sol.subsetXORSum(nums=[3, 4, 5, 6, 7, 8]))
