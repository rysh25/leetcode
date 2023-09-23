class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        """
        m x n の文字グリッド board と、文字列 word が与えられる。
        word がグリッドに存在したら true を返す。
        単語は、連続して隣接するセルの文字から構成できます。

        DFS で文字列を探索する。

        - Time complexity: O(l * nm)
            * `l' is length of `word'
        - Space complexity: O(nm)

        n は、nums の要素数を表します。

        #BackTracking
        #DFS

        Args:
            board (list[list[str]]): m x n の文字グリッド
            word (str): 文字列

        Returns:
            bool: word がグリッドに存在したら true を返す。
        """
        dx: list[int] = [1, 0, -1, 0]
        dy: list[int] = [0, 1, 0, -1]
        visited: list[list[bool]] = [[False] * len(board[0]) for _ in range(len(board))]

        def dfs(i: int, c: int, r: int) -> bool:
            if board[r][c] == word[i] and i == len(word) - 1:
                # print(f"found word={word}")
                return True
            elif board[r][c] != word[i]:
                return False

            # print(f"dfs: {word[i]}, i={i}, c={c}, r={r}")
            for di in range(4):
                nx = c + dx[di]
                ny = r + dy[di]
                if nx < 0 or ny < 0 or ny >= len(board) or nx >= len(board[ny]):
                    continue
                if visited[ny][nx]:
                    continue

                visited[ny][nx] = True
                # print(f"nx={nx}, ny={ny}")
                if dfs(i + 1, nx, ny):
                    return True
                visited[ny][nx] = False
            return False

        for r in range(len(board)):
            for c in range(len(board[r])):
                visited[r][c] = True
                if dfs(0, c, r):
                    return True
                visited[r][c] = False
        return False


sol = Solution()
print(
    sol.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCCED",
    )
)

print(
    sol.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="SEE",
    )
)

print(
    sol.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCB",
    )
)

print(
    sol.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]],
        word="ABCEFSADEESE",
    )
)
