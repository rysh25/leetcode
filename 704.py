from typing import List


def is_ok(v: int, target: int):
    if v >= target:
        return True
    return False


def lower_bound(nums: List[int], target: int) -> int:
    failure, ok = -1, len(nums)
    mid = -1
    while abs(ok - failure) > 1:
        mid = failure + (ok - failure) // 2
        if is_ok(nums[mid], target):
            ok = mid
        else:
            failure = mid
    return ok


def bin_search(nums: List[int], target: int) -> int:
    left, right = -1, len(nums)
    mid = -1
    while abs(right - left) > 1:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid
        else:
            left = mid
    return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        2分探索をする

        Time complexity: O(log n)
        Space complexity: O(1)
        """
        return bin_search(nums, target)


sol = Solution()
print(sol.search(nums=[-1, 0, 3, 5, 9, 12], target=9))
print(sol.search(nums=[-1, 0, 3, 5, 9, 12], target=8))
print(sol.search(nums=[-1, 0, 3, 5, 9, 12], target=2))
print(sol.search(nums=[-1, 0, 3, 5, 9, 12], target=-1))
print(sol.search(nums=[-1, 0, 3, 5, 9], target=-1))
print(sol.search(nums=[-1], target=-1))
print(sol.search(nums=[], target=-1))
