class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        2つの文字列 text1 と text2 が渡される。
        最も長い共通部分列の長さを返す。
        
        
        DP を行う。
        dp[i][j]には、text1[i-1]とtext2[j-1]までの中で最大の部分文字列の長さを格納する。

        - Time complexity: O(nm)
        - Space complexity: O(nm)

        #DP

        Args:
            text1 (str): 文字列
            text2 (str): 文字列

        Returns:
            int: 最も長い共通部分列の長さを返す。
        """

        dp: list[list[int]] = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[len(text1)][len(text2)]


sol = Solution()
print(sol.longestCommonSubsequence(text1="abcde", text2="ace"))
print(sol.longestCommonSubsequence(text1="abc", text2="abc"))
print(sol.longestCommonSubsequence(text1="abc", text2="def"))
