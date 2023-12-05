class Solution:
    def numberOfMatches(self, n: int) -> int:
        """
        奇妙なルールを持つトーナメントのチーム数を示す整数 n が与えられます。

        - 現在のチーム数が偶数の場合、各チームは別のチームとペアになります。 合計 n / 2 試合が行われ、n / 2 チームが次のラウンドに進みます。
        - 現在のチーム数が奇数の場合、1 つのチームがランダムにトーナメントに進み、残りのチームがペアになります。 合計 (n - 1) / 2 試合が行われ、(n - 1) / 2 + 1 チームが次のラウンドに進みます。

        勝者が決定するまでトーナメントで行われた試合数を返します。

        - Time complexicity: O(1)
        - Space complexicity: O(1)

        Args:
            n (int): チーム数を示す整数

        Returns:
            int: 勝者が決定するまでトーナメントで行われた試合数を返します。
        """
        return n - 1


sol = Solution()
print(sol.numberOfMatches(n=7))
print(sol.numberOfMatches(n=14))
