class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        arr: list[int] = []
        nums.sort()
        i = 0
        while i < len(nums):
            st: list[int] = []
            for _ in range(2):
                st.append(nums[i])
                i += 1
            while st:
                arr.append(st.pop())
        return arr


sol = Solution()
print(sol.numberGame(nums=[5, 4, 2, 3]))
print(sol.numberGame(nums=[2, 5]))
