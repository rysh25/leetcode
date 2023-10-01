class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        ans: int = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    ans = max(ans, (nums[i] - nums[j]) * nums[k])
        return ans


sol = Solution()
print(sol.maximumTripletValue(nums=[12, 6, 1, 2, 7]))
print(sol.maximumTripletValue(nums=[1, 10, 3, 4, 19]))
print(sol.maximumTripletValue(nums=[1, 2, 3]))
