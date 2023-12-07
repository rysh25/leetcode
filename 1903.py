class Solution:
    def largestOddNumber(self, num: str) -> str:
        """
        大きな整数を表す文字列 num が与えられます。
        num の空ではない部分文字列である最大値の奇数整数を (文字列として) 返します。
        奇数整数が存在しない場合は空の文字列 "" を返します。

        - Time complexity: O(n)
        - Space complexity: O(1)

        Args:
            num (str): 大きな整数を表す文字列

        Returns:
            str: num の空ではない部分文字列である最大値の奇数整数を (文字列として) 返します。
        """

        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[: i + 1]
        return ""


sol = Solution()
print(sol.largestOddNumber(num="52"))
print(sol.largestOddNumber(num="4206"))
print(sol.largestOddNumber(num="35427"))
