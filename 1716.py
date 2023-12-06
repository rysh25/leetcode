class Solution:
    def totalMoney(self, n: int) -> int:
        """
        ハーシーは初めての車のためにお金を節約したいと考えています。
        彼は毎日 LeetCode Bank にお金を預けています。

        彼は初日の月曜日に 1 ドルを投入することから始めます。
        火曜日から日曜日まで毎日、彼は前日よりも 1 ドル多く投資します。
        その後の毎週月曜日に、彼は前の月曜日よりも 1 ドル多く投入します。

        n が与えられた場合、n 日目の終わりに彼が Leetcode 銀行に持っている合計金額を返します。

        Args:
            n (int): 整数

        Returns:
            int: n 日目の終わりにハーシーが Leetcode 銀行に持っている合計金額を返します。
        """
        w = n // 7
        d = n % 7

        ans = 0
        for i in range(7):
            x = w
            if i < d:
                x += 1
            if x > 0:
                ans += (i + 1 + i + x) * x // 2
        return ans


sol = Solution()
print(sol.totalMoney(n=4))
print(sol.totalMoney(n=10))
print(sol.totalMoney(n=20))
