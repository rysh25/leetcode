class Solution:
    def modifiedMatrix(self, matrix: list[list[int]]) -> list[list[int]]:
        m = len(matrix[0])
        n = len(matrix)
        for j in range(m):
            mx = 0
            for i in range(n):
                # print(f"matrix[{i}][{j}]={matrix[i][j]}")
                mx = max(mx, matrix[i][j])

            for i in range(n):
                # print(f"matrix[{i}][{j}]={matrix[i][j]}")
                if matrix[i][j] == -1:
                    matrix[i][j] = mx

        return matrix


sol = Solution()
# print(sol.modifiedMatrix(matrix=[[1, 2, -1], [4, -1, 6], [7, 8, 9]]))
# print(sol.modifiedMatrix(matrix=[[3, -1], [5, 2]]))
print(
    sol.modifiedMatrix(
        matrix=[
            [-1, 0, 0, 2, 2],
            [2, 0, 0, 2, 1],
            [4, 3, 2, 1, 1],
            [-1, -1, 0, 2, 4],
            [1, 0, 3, -1, 0],
        ]
    )
)  # [[4,0,0,2,2],[2,0,0,2,1],[4,3,2,1,1],[4,3,0,2,4],[1,0,3,2,0]]
