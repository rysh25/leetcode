class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        符号なし整数のバイナリ表現を取得し、その整数が持つ「1」ビットの数 (ハミング重みとも呼ばれます) を返す関数を作成します。

        - Time complexity: O(n)
        - Space complexity: O(1)

        Args:
            n (int): 符号なし整数のバイナリ表現

        Returns:
            int: ハミング重み
        """
        ans = 0
        while n:
            if n & 1:
                ans += 1
            n >>= 1
        return ans


sol = Solution()
print(sol.hammingWeight(n=0b0000000000000000000000000001011))
print(sol.hammingWeight(n=0b0000000000000000000000010000000))
print(sol.hammingWeight(n=0b11111111111111111111111111111101))
