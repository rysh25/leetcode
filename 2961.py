class Solution:
    def getGoodIndices(self, variables: list[list[int]], target: int) -> list[int]:
        ans: list[int] = []
        for i in range(len(variables)):
            a, b, c, m = variables[i]
            if target == pow(pow(a, b, 10), c, m):
                ans.append(i)
        return ans


sol = Solution()
print(
    sol.getGoodIndices(variables=[[2, 3, 3, 10], [3, 3, 3, 1], [6, 1, 1, 4]], target=2)
)
print(sol.getGoodIndices(variables=[[39, 3, 1000, 1000]], target=17))
