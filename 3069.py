class Solution:
    def resultArray(self, nums: list[int]) -> list[int]:
        arr1: list[int] = [nums[0]]
        arr2: list[int] = [nums[1]]

        for i in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        return [*arr1, *arr2]


sol = Solution()
print(sol.resultArray(nums=[2, 1, 3]))
print(sol.resultArray(nums=[5, 4, 3, 8]))
