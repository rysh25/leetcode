from collections import deque


class Solution:
    def getWinner(self, arr: list[int], k: int) -> int:
        """
        相異なるの整数の配列 arr と整数 k が与えられます。

        ゲームは配列の最初の 2 つの要素 (つまり、arr[0] と arr[1]) の間で行われます。
        ゲームの各ラウンドで、arr[0] と arr[1] を比較します。
        大きいほうの整数が勝ち、位置 0 に残り、小さいほうの整数が配列の最後に移動します。
        k 回連続で勝利するとゲームは終了します。

        どの整数がゲームに勝つかを返します。

        ゲームの勝者が存在することが保証されています。


        queue を使ってシミュレーションを行います。
        ただし、arr.length<=10^5 かつ k<=10^9 という条件がある。
        k 回シミュレーションを行うと制限時間に間に合わない。
        arr の最大値は必ず勝つため、arr の最大値の順番になった場合、そこでシミュレーションを
        打ち切る。そうることで最大 arr.length の回数までで収まる。


        - Time complexity: O(n)
        - Space complexity: O(n)

        Args:
            arr (list[int]): 相異なるの整数の配列
            k (int): 整数

        Returns:
            int: どの整数がゲームに勝つかを返します。
        """
        max_element = max(arr)
        q: deque[int] = deque(arr[1:])
        curr = arr[0]

        winstreak = 0
        while winstreak < k and curr != max_element:
            opponent = q.popleft()
            if curr > opponent:
                winstreak += 1
                q.append(opponent)
            else:
                q.append(curr)
                curr = opponent
                winstreak = 1

        return curr


sol = Solution()
print(sol.getWinner(arr=[2, 1, 3, 5, 4, 6, 7], k=2))
print(sol.getWinner(arr=[3, 2, 1], k=10))
