import math


class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        max_dia: float = 0
        max_area = 0
        for i in range(len(dimensions)):
            dia = math.sqrt(
                dimensions[i][0] * dimensions[i][0]
                + dimensions[i][1] * dimensions[i][1]
            )
            area = dimensions[i][0] * dimensions[i][1]
            if max_dia < dia or (dia == max_dia and max_area < area):
                max_dia = dia
                max_area = area

        return max_area


sol = Solution()
print(sol.areaOfMaxDiagonal(dimensions=[[9, 3], [8, 6]]))
print(sol.areaOfMaxDiagonal(dimensions=[[3, 4], [4, 3]]))
print(sol.areaOfMaxDiagonal(dimensions=[[1, 1]]))
