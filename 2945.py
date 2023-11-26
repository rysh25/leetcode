class Solution:
    def findMaximumLength(self, nums: list[int]) -> int:
        n = len(nums)
        print(f"nums={nums}")
        prefix_sum: list[int] = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        print(f"prefix_sum={prefix_sum}")

        ans = n
        i = 1
        while i < n:
            j = i
            print(
                f"i={i}, nums[i - 1]={nums[i - 1]}, prefix_sum[j + 1]={prefix_sum[j + 1]}, prefix_sum[i]={prefix_sum[i]}"
            )
            while j + 1 <= n and nums[i - 1] >= prefix_sum[j + 1] - prefix_sum[i]:
                print(
                    f"i={i}, nums[i - 1]={nums[i - 1]}, prefix_sum[j + 1]={prefix_sum[j + 1]}, prefix_sum[i]={prefix_sum[i]}"
                )
                j += 1
            print(f"i={i}, j={j}")
            ans -= j - i
            i = j + 1
        return ans


sol = Solution()
# print(sol.findMaximumLength(nums=[5, 2, 2]))
# print(sol.findMaximumLength(nums=[1, 2, 3, 4]))
# print(sol.findMaximumLength(nums=[4, 3, 2, 6]))
print(sol.findMaximumLength([980, 973, 229, 51, 594]))  # 2
