class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        """
        整数 n が与えられた場合、
        次の操作を何度でも使用して、それを 0 に変換する必要があります。

        - n のバイナリ表現の右端 (0 番目) ビットを変更します。
        - (i-1) 番目のビットが 1 に設定され、
          (i-2) 番目から 0 番目のビットが 0 に設定されている場合、
          n の 2 進数表現の i 番目のビットを変更します。

        n を 0 に変換するための演算の最小数を返します。


        - Time complexity: O(log n)
        - Space complexity: O(n)

        Args:
            n (int): 整数 n が与えられる

        Returns:
            int: n を 0 に変換するための演算の最小数を返します。
        """
        res = 0
        while n:
            res = -res - (n ^ (n - 1))
            n &= n - 1
        return abs(res)


sol = Solution()
print(sol.minimumOneBitOperations(n=3))
print(sol.minimumOneBitOperations(n=6))
