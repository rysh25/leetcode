class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        """
        一意の整数の配列 arr が渡される。
        整数 arr[i] は、1より大きい。
        これらの整数を使って、バイナリーツリーを作る。
        それぞれの数値は何度も使える。
        葉でないノードの値は、その子供の値の積と同じでなければならない。
        作成することができるバイナリーツリーの数を返す。 答えは、10^9+7 を法とする。


        1次元のDPを行う。
        dp[i] には、arr[i] をルートとするバイナリーツリーの数をカウントする。
        各ノードは、子供がないバイナリーツリーを作ることができるため、1で初期化する。
        大きい値が小さい値の親になることはないため、まず arr をソートする。
        さらに、この後利用するためにarr のインデックスを辞書に記録する。

        i,jの二重ループとし、を iを1からn-1まで、jを0 から i-1までループする
        jをiの子供にできるかを調べる。arr[i]をarr[j]で割ったあまりが0であり、
        arr[i]//arr[j]がmap に存在すれば、arr[i]がarr[j]とarr[i]//arr[j]のルートとなることができることを表す。
        dp[i] に、dpの j と辞書から取得したarr[i]//arr[j]のインデックスの値をかけたものをたす。
        これは、左右の子がルートとなるバイナリーツリーのパターンの数であるためかけたものがその親のパターン数となる。

        最後に、dp すべての値を合計したものが答えとなる。

        - Time complexity: O(n^2)
        - Space complexity: O(n^2)

        #DP

        Args:
            arr (list[int]): 一意の整数の配列 arr が渡される。

        Returns:
            int: 作成することができるバイナリーツリーの数を返す。
        """
        n = len(arr)
        MOD = 10**9 + 7
        arr.sort()
        dp: list[int] = [1] * n
        m: dict[int, int] = {arr[i]: i for i in range(n)}

        for i in range(1, n):
            for j in range(i):
                if arr[i] % arr[j] != 0:
                    continue
                if arr[i] // arr[j] not in m:
                    continue
                dp[i] += dp[j] * dp[m[arr[i] // arr[j]]] % MOD

        return sum(dp) % MOD


sol = Solution()
print(sol.numFactoredBinaryTrees(arr=[2, 4]))
print(sol.numFactoredBinaryTrees(arr=[2, 4, 5, 10]))
