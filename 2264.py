class Solution:
    def largestGoodInteger(self, num: str) -> str:
        """
        大きな整数を表す文字列 num が与えられます。 次の条件を満たす場合、整数が good です。

        - 長さ 3 の num の部分文字列です。
        - 1 つの固有の数字のみで構成されます。

        最大の good な整数を文字列として返すか、そのような整数が存在しない場合は空の文字列 "" を返します。

        - Time complexity: O(n)
        - Space complexity: O(1)

        Args:
            num (str): 大きな整数を表す文字列 num が与えられます。

        Returns:
            str: 最大の good な整数を文字列として返すか、そのような整数が存在しない場合は空の文字列 "" を返します。
        """

        ans = ""
        streak = 0
        prev = ""
        for n in num:
            if n == prev:
                streak += 1
            else:
                streak = 1
            # print(f"n={n}, streak={streak}")

            if streak == 3:
                ans = max(ans, n * streak)

            prev = n

        return ans


sol = Solution()
print(sol.largestGoodInteger(num="6777133339"))
print(sol.largestGoodInteger(num="2300019"))
print(sol.largestGoodInteger(num="42352338"))
