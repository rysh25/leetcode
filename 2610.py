class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        ans: list[list[int]] = []
        freq: list[int] = [0] * (len(nums) + 1)

        for i in nums:
            if freq[i] >= len(ans):
                ans.append([])

            ans[freq[i]].append(i)
            freq[i] += 1

        return ans


sol = Solution()
print(sol.findMatrix(nums=[1, 3, 4, 1, 2, 3, 1]))
print(sol.findMatrix(nums=[1, 2, 3, 4]))
