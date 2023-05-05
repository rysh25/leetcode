from typing import List


class Solution_bs:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def bin_search(nums: List[int], t: int, exclude: int) -> int:
            left = -1
            right = len(nums)
            while right - left > 1:
                m = left + (right - left) // 2
                if exclude != m and t == nums[m]:
                    return m
                elif t < nums[m]:
                    right = m
                else:
                    left = m

            return -1

        for i, num in enumerate(numbers):
            if (found := bin_search(numbers, target - num, i)) != -1:
                return [i + 1, found + 1]

        return []


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            num = numbers[left] + numbers[right]
            if num == target:
                return [left + 1, right + 1]
            elif num > target:
                right -= 1
            else:
                left += 1
        return []


sol = Solution()
print(sol.twoSum(numbers=[2, 7, 11, 15], target=9))
print(sol.twoSum(numbers=[2, 3, 4], target=6))
print(sol.twoSum(numbers=[5, 25, 75], target=100))
print(sol.twoSum(numbers=[5, 25, 75], target=101))
print(sol.twoSum(numbers=[1, 2, 3, 4, 4, 9, 56, 90], target=8))
