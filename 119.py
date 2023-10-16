class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        """
        整数 rowIndex が与えられ、0インデックスで、rowIndex 番目の
        パスカルの三角形の行を返す。

        Args:
            rowIndex (int): 整数が与えられる。

        Returns:
            list[int]: rowIndex 番目のパスカルの三角形の行を返す。
        """
        pascalsTriangle: list[int] = []
        ans: list[int] = []
        for r in range(0, rowIndex + 1):
            # print(f"r={r}")
            for c in range(r + 1):
                # print(f"c={c}")
                if c == 0 or c == r:
                    pascalsTriangle.append(1)
                else:
                    pascalsTriangle.append(
                        pascalsTriangle[-(r + 1)] + pascalsTriangle[-r]
                    )
                # print(f"{pascalsTriangle[-1]}", end=" ")
                if r == rowIndex:
                    ans.append(pascalsTriangle[-1])
            # print()
        return ans


sol = Solution()
print(sol.getRow(rowIndex=3))
print(sol.getRow(rowIndex=0))
print(sol.getRow(rowIndex=1))
print(sol.getRow(rowIndex=4))
print(sol.getRow(rowIndex=5))
