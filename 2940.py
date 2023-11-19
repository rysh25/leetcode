class Solution:
    def leftmostBuildingQueries(
        self, heights: list[int], queries: list[list[int]]
    ) -> list[int]:
        ans: list[int] = [0] * len(heights)
        stack: list[tuple[int, int]] = [(-1, 0)]  # (index, heigth)
        heights.append(0)

        for index, height in enumerate(heights):
            while stack and height > stack[-1][1]:
                i, _ = stack.pop()
                ans[i] = index - i

            stack.append((index, height))

        print(f"ans={ans}")

        ans: list[int] = []

        for query in queries:
            pass

        return ans


sol = Solution()
print(
    sol.leftmostBuildingQueries(
        heights=[6, 4, 8, 5, 2, 7], queries=[[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]]
    )
)
print(
    sol.leftmostBuildingQueries(
        heights=[5, 3, 8, 2, 6, 1, 4, 6],
        queries=[[0, 7], [3, 5], [5, 2], [3, 0], [1, 6]],
    )
)
