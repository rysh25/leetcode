from typing import List


# https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -(10**18)  # これまでの連続部分配列の和の最大値
        tmp = 0  # 現在のインデックスを利用した連続部分配列の和の最大値
        for i in range(len(nums)):
            tmp = max(tmp + nums[i], nums[i])
            ans = max(ans, tmp)

        return ans


sol = Solution()
print(sol.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
