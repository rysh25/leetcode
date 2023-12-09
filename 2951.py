class Solution:
    def findPeaks(self, mountain: list[int]) -> list[int]:
        ans: list[int] = []
        for i in range(1, len(mountain) - 1):
            if mountain[i - 1] < mountain[i] > mountain[i + 1]:
                ans.append(i)
        return ans


sol = Solution()
print(sol.findPeaks(mountain=[2, 4, 4]))
print(sol.findPeaks(mountain=[1, 4, 3, 8, 5]))
