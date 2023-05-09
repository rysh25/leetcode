from typing import List, Tuple


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        整数の配列から、その全ての連続部分列 (subarray) の最小値の合計を計算する。
        その結果を10^9+7で法として返す。

        全ての連続部分列を生成し、全探索する場合、O(N^2) となり間に合わない。
        部分列の最小値を求めるて合計を計算する代わりに、各値を基準として、最小となる部分列の数を求める。

        配列最初からループするこの値が基準として、この値が含まれる連続部分列の個数を求めていく。
        最小部分列の数は、単調減少スタック (Monotonic Decreasing Stack) を使用して求める。

        #Stack
        #MonotonicStack
        """

        MOD = 10**9 + 7
        stack: List[Tuple[int, int]] = []  # (value, count)
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
