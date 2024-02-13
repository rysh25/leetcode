class Solution:
    def countMatchingSubarrays(self, nums: list[int], pattern: list[int]) -> int:
        n = len(nums)
        m = len(pattern)
        p: list[int] = [0] * (n - 1)
        # print(f"m={m}, pattern={pattern}")

        for i in range(n - 1):
            if nums[i] < nums[i + 1]:
                p[i] = 1
            elif nums[i] == nums[i + 1]:
                p[i] = 0
            else:
                p[i] = -1

        # print(f"p={p}")

        ans = 0
        for i in range(n - m):
            # print(f"i={i}")
            match = True
            for j in range(m):
                # print(f"j={j}, pattern[j]={pattern[j]} != p[i + j]={p[i + j]}")
                if pattern[j] != p[i + j]:
                    match = False
                    break

            if match:
                # print(f"m:")
                ans += 1

        return ans


sol = Solution()
print(sol.countMatchingSubarrays(nums=[1, 2, 3, 4, 5, 6], pattern=[1, 1]))
print(sol.countMatchingSubarrays(nums=[1, 4, 4, 1, 3, 5, 5, 3], pattern=[1, 0, -1]))
