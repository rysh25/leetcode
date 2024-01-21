class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        freq: list[int] = [0] * 101

        for i in nums:
            freq[i] += 1

        # print(f"freq={freq}")
        mx = max(freq)
        # print(f"mx={mx}")

        ans = 0
        for i in freq:
            if i == mx:
                ans += i

        return ans


sol = Solution()
print(sol.maxFrequencyElements(nums=[1, 2, 2, 3, 1, 4]))
print(sol.maxFrequencyElements(nums=[1, 2, 3, 4, 5]))
print(sol.maxFrequencyElements(nums=[10, 12, 11, 9, 6, 19, 11]))  # 2
