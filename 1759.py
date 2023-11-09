class Solution:
    def countHomogenous(self, s: str) -> int:
        """
        文字列 s を指定すると、s の同種の部分文字列の数を返します。
        答えが大きすぎる可能性があるため、10^9 + 7 を法にして返します。

        文字列のすべての文字が同じである場合、その文字列は同種です。

        部分文字列は、文字列内の連続した文字のシーケンスです。


        同種の部分文字列の数は、同種の部分文字列の streak(streak+1)/2 の合計
        で求めることができる。

        Time complexity: O(n)
        Space complexity: O(1)

        Args:
            s (str): 文字列

        Returns:
            int: s の同種の部分文字列の数を返します。
        """
        MOD = 10**9 + 7
        prev = ""
        streak = 0
        ans = 0
        for i in range(len(s)):
            if prev == s[i]:
                streak += 1
            else:
                ans += (1 + streak) * streak // 2 % MOD
                streak = 1
            prev = s[i]

        ans += (1 + streak) * streak // 2 % MOD
        return ans


sol = Solution()
print(sol.countHomogenous(s="abbcccaa"))
print(sol.countHomogenous(s="xy"))
print(sol.countHomogenous(s="zzzzz"))
