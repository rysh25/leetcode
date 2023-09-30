class Solution_memo:
    def numDecodings(self, s: str) -> int:
        """
        メッセージは、数字にエンコード可能な A-Z の文字からなる
        デコード数には、この反対を行い数字を文字にマッピングする。
        そのには複数の方法がある可能性がある。
        数字のみからなる文字列 s が渡される。デコードする方法の数を返す。

        各文字、1文字選ぶ、2文字選ぶの2通りの分岐を行う。

        単純な実装では、O(n^2) となるがメモ化再帰を行うことで、実行時間を抑える。

        - Time complexity: O(n)
        - Space complexity: O(n)

        #DFS
        #Memolization

        Args:
            s (str): 数字のみからなる文字列 s が渡される。

        Returns:
            int: デコードする方法の数を返す。
        """
        memo: list[int] = [-1] * len(s)

        def dfs(i: int) -> int:
            # print(f"i={i}")
            if i == len(s):
                # print(f"found")
                return 1

            if memo[i] >= 0:
                return memo[i]

            if s[i] == "0":
                return 0

            count = 0
            if i + 1 <= len(s) and s[i] != "0":
                count += dfs(i + 1)

            if i + 2 <= len(s) and int(s[i : i + 2]) < 27:
                count += dfs(i + 2)

            memo[i] = count

            return count

        # print(f"s={s}")
        return dfs(0)


class Solution:
    def numDecodings(self, s: str) -> int:
        """
        メッセージは、数字にエンコード可能な A-Z の文字からなる
        デコード数には、この反対を行い数字を文字にマッピングする。
        そのには複数の方法がある可能性がある。
        数字のみからなる文字列 s が渡される。デコードする方法の数を返す。

        各文字、1文字選ぶ、2文字選ぶの2通りの分岐を行う。

        単純な実装では、O(n^2) となるが動的計画法で、実行時間を抑える。

        - Time complexity: O(n)
        - Space complexity: O(n)

        #DP

        Args:
            s (str): 数字のみからなる文字列 s が渡される。

        Returns:
            int: デコードする方法の数を返す。
        """
        dp: list[int] = [0] * (len(s) + 1)
        dp[-1] = 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            elif i + 1 < len(s) and int(s[i]) < int(s[i : i + 2]) < 27:
                dp[i] = dp[i + 1] + dp[i + 2]
            else:
                dp[i] = dp[i + 1]

        return dp[0]


sol = Solution()
print(sol.numDecodings(s="12"))
print(sol.numDecodings(s="226"))
print(sol.numDecodings(s="06"))
print(sol.numDecodings(s="10"))
