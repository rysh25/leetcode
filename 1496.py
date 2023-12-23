class Solution:
    def isPathCrossing(self, path: str) -> bool:
        """
        文字列 path が渡されます。これは、path[i] = 'N'、'S'、'E'、または 'W' となり、
        それぞれ北、南、東、または西に 1 単位移動することを表します。
        2次元平面上の原点 (0, 0) から開始し、path で指定されたパス上を歩きます。

        パスがどこかの時点で交差する場合、つまり、以前に訪れたことのある場所にいる場合は、true を返します。
        それ以外の場合は false を返します。

        - Time complexity: O(n)
        - Space complexity: O(n)

        Args:
            path (str): 'N'、'S'、'E'、または 'W' からなる文字列

        Returns:
            bool: パスがどこかの時点で交差する場合、つまり、以前に訪れたことのある場所にいる場合は、true を返します。それ以外の場合は false を返します。
        """
        visited: set[tuple[int, int]] = set()

        curr: tuple[int, int] = (0, 0)
        visited.add(curr)
        for i in range(len(path)):
            if path[i] == "N":
                curr = (curr[0], curr[1] + 1)
            elif path[i] == "S":
                curr = (curr[0], curr[1] - 1)
            elif path[i] == "E":
                curr = (curr[0] + 1, curr[1])
            elif path[i] == "W":
                curr = (curr[0] - 1, curr[1])
            if curr in visited:
                return True
            visited.add(curr)
        return False


sol = Solution()
print(sol.isPathCrossing(path="NES"))
print(sol.isPathCrossing(path="NESWW"))
