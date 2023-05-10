class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        """
        整数の配列から、その全ての連続部分列 (subarray) の最小値の合計を計算します。
        その結果を10^9+7を法として返します。

        全ての連続部分列を生成し、全探索する場合、O(N^2) となり間に合いません。
        部分列の最小値を求めるて合計を計算する代わりに、各値を基準として、最小となる部分列の数を求めます。

        配列最初からループする。この値が基準として、この値が含まれる連続部分列の個数を求めていきます。
        最小部分列の数は、単調減少スタック (Monotonic Decreasing Stack) を使用して求めます。

        #Stack
        #MonotonicStack

        Args:
            heights (list[int]): ヒストグラムのバーの高さからなる整数の配列を渡します。

        Returns:
            int: ヒストグラムの最大の面積を返します。
        """

        MOD = 10**9 + 7
        stack: list[tuple[int, int]] = []  # (value, count)
        res = 0
        prevsum = 0

        for value in arr:
            print(f"value={value}")
            count = 1
            while stack and stack[-1][0] >= value:
                v, c = stack.pop()
                print(f"v={v}, c={c}")
                count += c
                prevsum -= v * c
            stack.append((value, count))
            print(f"push: value={value}, count={count}, prevsum={prevsum}")
            prevsum += value * count
            res += prevsum

        return res % MOD


sol = Solution()
print(sol.sumSubarrayMins(arr=[3, 1, 2, 4]))
# print(sol.sumSubarrayMins(arr=[11, 81, 94, 43, 3]))
