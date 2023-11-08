class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        """
        4 つの整数 sx、sy、fx、fy、および非負の整数 t が与えられます。

        無限 2D グリッドでは、セル (sx、sy) から開始します。 毎秒、隣接するセルのいずれかに移動する必要があります。

        ちょうど t 秒後にセル (fx, fy) に到達できる場合は true を返し、それ以外の場合は false を返します。

        セルの隣接セルとは、少なくとも 1 つの角を共有する周囲の 8 つのセルです。 同じセルに複数回アクセスできます。


        開始と終了が同じ位置なら時間が1以外なら到達可能
        開始と終了が別の位置なら、距離が時間以上なら到達可能
        それ以外は到達不可能

        - Time complexity: O(1)
        - Space complexity: O(1)

        Args:
            sx (int): 開始セルの x 座標を表す整数
            sy (int): 開始セルの y 座標を表す整数
            fx (int): 最終セルの x 座標を表す整数
            fy (int): 最終セルの y 座標を表す整数
            t (int): 秒を表す非負整数

        Returns:
            bool: ちょうど t 秒後にセル (fx, fy) に到達できる場合は true を返し、それ以外の場合は false を返します。
        """
        if sx == fx and sy == fy:
            return True if t != 1 else False
        d = max(abs(fx - sx), abs(fy - sy))
        # print(f"d={d}, t={t}, t-d={t-d}")
        return True if t - d >= 0 else False


sol = Solution()
print(sol.isReachableAtTime(sx=2, sy=4, fx=7, fy=7, t=6))
print(sol.isReachableAtTime(sx=3, sy=1, fx=7, fy=3, t=3))
print(sol.isReachableAtTime(sx=1, sy=2, fx=1, fy=2, t=1))  # False
print(sol.isReachableAtTime(sx=1, sy=1, fx=1, fy=1, t=3))  # True
print(sol.isReachableAtTime(sx=1, sy=1, fx=1, fy=3, t=2))  # True
print(sol.isReachableAtTime(sx=1, sy=3, fx=1, fy=3, t=0))  # True
