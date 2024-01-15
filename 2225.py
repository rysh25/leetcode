class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        """
        整数配列のmatchesが与えられます。
        matches[i] = [winer_i, Loser_i]は、試合で winner_i プレイヤーが loser_i プレイヤーに勝ったことを示します。

        サイズ 2 の answer のリストを返します。ここで、

        - answer[0] は、試合に負けていないすべてのプレイヤーのリストです。
        - answer[1] は、ちょうど 1 試合で負けたすべてのプレイヤーのリストです。

        2 つのリストの値は昇順で返される必要があります。

        - Time complexity: O(n)
        - Space complexity: O(1)

        Args:
            matches (list[list[int]]): 整数配列

        Returns:
            list[list[int]]: answer のリストを返します
        """
        INF = 10**9 + 1
        losts: list[int] = [-INF] * (10**5 + 1)

        for match in matches:
            if losts[match[0]] < 0:
                losts[match[0]] = 0
            if losts[match[1]] < 0:
                losts[match[1]] = 1
            else:
                losts[match[1]] += 1

        ans: list[list[int]] = [[] for _ in range(2)]

        for i in range(len(losts)):
            if losts[i] == 0:
                ans[0].append(i)
            elif losts[i] == 1:
                ans[1].append(i)

        return ans


sol = Solution()
print(
    sol.findWinners(
        matches=[
            [1, 3],
            [2, 3],
            [3, 6],
            [5, 6],
            [5, 7],
            [4, 5],
            [4, 8],
            [4, 9],
            [10, 4],
            [10, 9],
        ]
    )
)
print(sol.findWinners(matches=[[2, 3], [1, 3], [5, 4], [6, 4]]))
