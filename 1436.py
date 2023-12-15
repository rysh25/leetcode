class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        """
        配列 path が与えられます。
        ここで、 paths[i] = [cityAi, cityBi] は、cityAi から cityBi へ向かう直接パスが存在することを意味します。
        目的地の都市、つまり別の都市への経路を持たない都市を返します。

        path のグラフがループのない線を形成することが保証されているため、目的地の都市は 1 つだけになります。

        - Time complexity: O(n)
        - Space complexity: O(n)

        Args:
            paths (list[list[str]]): 直接パス

        Returns:
            str: 別の都市への経路を持たない都市を返します。
        """
        not_ans: set[str] = set()

        for path in paths:
            not_ans.add(path[0])

        for path in paths:
            if path[1] not in not_ans:
                return path[1]

        return ""


sol = Solution()
print(
    sol.destCity(
        paths=[["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
    )
)
print(sol.destCity(paths=[["B", "C"], ["D", "B"], ["C", "A"]]))
print(sol.destCity(paths=[["A", "Z"]]))
