class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        n = len(nums)
        ans: list[list[int]] = []
        nums.sort()
        for i in range(n):
            if i % 3 == 0:
                ans.append([nums[i]])
            elif i % 3 == 1 or i % 3 == 2:
                if nums[i] - ans[-1][0] <= k:
                    ans[-1].append(nums[i])
                else:
                    return []

        return ans


sol = Solution()
print(sol.divideArray(nums=[1, 3, 4, 8, 7, 9, 3, 5, 1], k=2))
print(sol.divideArray(nums=[1, 3, 3, 2, 7, 3], k=3))

print(
    sol.divideArray(
        nums=[
            15,
            13,
            12,
            13,
            12,
            14,
            12,
            2,
            3,
            13,
            12,
            14,
            14,
            13,
            5,
            12,
            12,
            2,
            13,
            2,
            2,
        ],
        k=2,
    )
)
