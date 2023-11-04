class Solution:
    def findKOr(self, nums: list[int], k: int) -> int:
        ans = 0
        for i in range(31):
            bit = 1 << i
            # print(f"bit={bit}")
            count = 0
            for num in nums:
                if num >= 0 and (bit & num) != 0:
                    # print(f"bit={bit}, num={num}")
                    count += 1
            if count >= k:
                ans += bit
        return ans


sol = Solution()
print(sol.findKOr(nums=[7, 12, 9, 8, 9, 15], k=4))
print(sol.findKOr(nums=[2, 12, 1, 11, 4, 5], k=6))
print(sol.findKOr(nums=[10, 8, 5, 9, 11, 6, 8], k=1))
