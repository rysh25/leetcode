class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        max_increasing_length = 0
        max_decreasing_length = 0
        ans = 0
        prev = -1
        for i in nums:
            # print(
            #     f"i={i}, prev={prev}, max_increasing_length={max_increasing_length}, max_decreasing_length={max_decreasing_length}"
            # )
            if prev == -1:
                # print(f"1:")
                max_increasing_length += 1
                max_decreasing_length += 1
            elif prev < i:
                # print(f"2:")
                max_increasing_length += 1
                max_decreasing_length = 1
            elif prev > i:
                # print(f"3:")
                max_increasing_length = 1
                max_decreasing_length += 1
            else:
                # print(f"4:")
                max_increasing_length = 1
                max_decreasing_length = 1

            prev = i
            ans = max(ans, max_increasing_length, max_decreasing_length)

        return ans


sol = Solution()
print(sol.longestMonotonicSubarray(nums=[1, 4, 3, 3, 2]))
print(sol.longestMonotonicSubarray(nums=[3, 3, 3, 3]))
print(sol.longestMonotonicSubarray(nums=[3, 2, 1]))
print(sol.longestMonotonicSubarray(nums=[1, 10, 10]))
