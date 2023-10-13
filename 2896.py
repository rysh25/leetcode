class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        """_summary_
        2つの同じ長さ n の0インデックスのバイナリ文字列 s1 と s2 と、正の整数 x が渡される。

        s1 に、次の操作何度でも実行できる。:

        - 2つのインデックス i と j を選んで、その両方を裏返す。そのコストは x。
        - 1つのインデックス i (i < n - 1) を選んで、s1[i] と s[i+1] を裏返す。そのコストは１。

        s1 と s2 が等しくするのに必要な最小のコストを返す。不可能なら -1 を返す。

        s1 と s2 の各インデックスの要素が異なる数が奇数なら不可能なため -1 を返す。

        diff 配列に、str1 と str2 の要素が異なるのインデックスを記録する。
        異る要素(iとする)から、次に異なる要素(jとする)までを一致させる最小のコストは、
        j - i (i+1 を jまで順番に裏返す)か、x (一度に裏返す)の小さい方となる。


        - Time complexity: O(n)
        - Space complexity: O(n)

        Args:
            s1 (str): バイナリ文字列
            s2 (str): バイナリ文字列
            x (int): 正の整数 x

        Returns:
            int: s1 と s2 が等しくするのに必要な最小のコストを返す。不可能なら -1 を返す。
        """

        print(f"s1={s1}, s2={s2}, x={x}")
        diff = [i for i in range(len(s1)) if s1[i] != s2[i]]
        print(f"diff={diff}")

        if len(diff) == 0:
            return 0

        if len(diff) % 2 != 0:
            return -1

        dp: list[int] = [0] * (len(diff))

        for i in range(1, len(diff)):
            dp[i] = min(diff[i] - diff[i - 1], x) + dp[i - 1]

        print(f"dp={dp}")

        return dp[len(diff) - 2]


sol = Solution()
print(sol.minOperations(s1="1010", s2="0101", x=2))
print(sol.minOperations(s1="1100011000", s2="0101001010", x=2))
print(sol.minOperations(s1="10110", s2="00011", x=4))
print(sol.minOperations(s1="101101", s2="000000", x=6))  # 4
print(sol.minOperations(s1="11001011111", s2="01111000110", x=2))  # 4
