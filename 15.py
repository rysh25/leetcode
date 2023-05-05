from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print(f"nums={nums}")

        ans: List[List[int]] = []

        for i, target in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                # print(f"i={i}, left={left}, right={right}")
                n = target + nums[left] + nums[right]
                if n == 0:
                    ans.append([target, nums[left], nums[right]])
                    right -= 1
                    while True:
                        left += 1
                        if nums[left] != nums[left - 1] or left >= right:
                            break
                elif n > 0:
                    right -= 1
                else:
                    left += 1

        return ans


sol = Solution()
print(sol.threeSum(nums=[-1, 0, 1, 2, -1, -4]))
print(sol.threeSum(nums=[0, 1, 1]))
print(sol.threeSum(nums=[0, 0, 0]))
print(sol.threeSum(nums=[-2, 0, 1, 1, 2]))  # [[-2, 0, 2], [-2, 1, 1]]
print(sol.threeSum(nums=[-2, 0, 0, 2, 2]))  # [[-2,0,2]]
