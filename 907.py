class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        """
        整数の配列から、その全ての連続部分列 (subarray) の最小値の合計を計算します。
        その結果を10^9+7を法として返します。


        全ての連続部分列を生成し、全探索する場合、O(N^2) となり間に合わない。
        部分列の最小値を求めるて合計を計算する代わりに、各値を基準として、最小となる部分配列の数を求る。
        各値を基準として、最小となる部分配列の数は、「その値をより右の小さい値の手前までの個数」*「その値より左の小さい値の手前までの個数」となる。

        単調減少スタック (Monotonic Decreasing Stack) を使用して、
        配列の「その値をより右の小さい値の手前までインデックス」と「その値より左の小さい値の手前までのインデックス」を求め、それぞれ、left 配列、right 配列に入れる。

        - Time complexity: O(n)
        - Space complexity: O(n)

        #Stack
        #MonotonicStack

        Args:
            arr (list[int]): 整数の配列

        Returns:
            int: 整数の配列から、その全ての連続部分列 (subarray) の最小値の合計を計算します。その結果を10^9+7を法として返します。
        """
        print(f"arr={arr}")
        n = len(arr)
        MOD = 10**9 + 7
        left: list[int] = [0] * n
        right: list[int] = [n - 1] * n
        st: list[tuple[int, int]] = []  # (value, index)

        for i in range(n):
            while st and st[-1][0] >= arr[i]:
                _, si = st.pop()
                right[si] = i - 1

            if st:
                left[i] = st[-1][1] + 1
            st.append((arr[i], i))

        # print(f"left={left}, right={right}")

        ans = 0

        for i in range(n):
            ans += arr[i] * (i - left[i] + 1) * (right[i] - i + 1) % MOD

        return ans % MOD


sol = Solution()
print(sol.sumSubarrayMins(arr=[3, 1, 2, 4]))
print(sol.sumSubarrayMins(arr=[11, 81, 94, 43, 3]))
