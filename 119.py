class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        """
        整数 rowIndex が与えられ、0インデックスで、rowIndex 番目の
        パスカルの三角形の行を返す。

        組み合わせの公式を使って求める。

        - Time complexity: O(n)
        - Time complexity: O(n)

        Args:
            rowIndex (int): 整数が与えられる。

        Returns:
            list[int]: rowIndex 番目のパスカルの三角形の行を返す。
        """
        ans: list[int] = [1]
        prev = 1
        for k in range(1, rowIndex + 1):
            next = prev * (rowIndex - k + 1) // k
            ans.append(next)
            prev = next

        return ans


sol = Solution()
print(sol.getRow(rowIndex=3))
print(sol.getRow(rowIndex=0))
print(sol.getRow(rowIndex=1))
print(sol.getRow(rowIndex=4))
print(sol.getRow(rowIndex=5))
