class Solution:
    def getLastMoment(self, n: int, left: list[int], right: list[int]) -> int:
        """
        長さ n 単位の木の板があります。 数匹のアリが板の上を歩いており、各アリは 1 秒あたり 1 単位の速度で移動します。 一部のアリは左に移動し、他のアリは右に移動します。

        異なる方向に移動する2匹のアリがある時点で出会うと、方向を変えて再び移動を続けます。 方向転換には追加の時間はかからないと仮定します。

        アリが時間 t に板の一端に到達すると、すぐに板から落ちます。

        整数 n と左右の 2 つの整数配列をが渡されます。
        左右に移動するアリの位置によって、最後のアリが板から落ちる瞬間を返します。


        右に進むアリと左に進むアリが出会った瞬間に方向を入れ替えるのは、そのまま素通りすると見なすことができる。
        そのため端までの距離が一番あるアリが端に到達するまでの時間が、最後のアリが板から落ちる時間となる。

        Args:
            n (int): 板の長さ
            left (list[int]): 左に進むアリの位置
            right (list[int]): 右に進むアリの位置

        Returns:
            int: 最後のアリが板から落ちる瞬間を返します。
        """
        return max(n - min(right, default=n), max(left, default=0))


sol = Solution()
print(sol.getLastMoment(n=4, left=[4, 3], right=[0, 1]))
print(sol.getLastMoment(n=7, left=[], right=[0, 1, 2, 3, 4, 5, 6, 7]))
print(sol.getLastMoment(n=7, left=[0, 1, 2, 3, 4, 5, 6, 7], right=[]))
print(sol.getLastMoment(n=1000, left=[0], right=[]))  # 0
print(sol.getLastMoment(n=1000, left=[], right=[]))  # 0
