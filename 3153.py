class Solution:
    def sumDigitDifferences(self, nums: list[int]) -> int:
        n = len(nums)
        num_digits = len(str(nums[0]))

        digit_counts = [[0] * 10 for _ in range(num_digits)]

        for num in nums:
            num_str = str(num)
            for i in range(num_digits):
                digit_counts[i][int(num_str[i])] += 1

        ans = 0

        for i in range(num_digits):
            for d1 in range(10):
                d1_count = digit_counts[i][d1]
                if d1_count == 0:
                    continue
                # print(f"i={i}, d1={d1}, d1_count={d1_count}")

                ans += d1_count * (n - d1_count)

                # for d2 in range(10):
                #     if d1 == d2:
                #         continue
                #     d2_count = digit_counts[i][d2]

                #     if d2_count > 0:
                #         # print(
                #         #     f"i={i}, d2={d2}, d2_count={d2_count}, abs(d1 - d2)={abs(d1 - d2)}, abs(d1 - d2) * d2_count={abs(d1 - d2) * d2_count}"
                #         # )

                #         ans += abs(d1 - d2) * d1_count * d2_count

        return ans // 2


sol = Solution()
print(sol.sumDigitDifferences(nums=[13, 23, 12]))
print(sol.sumDigitDifferences(nums=[10, 10, 10, 10]))
print(sol.sumDigitDifferences(nums=[56, 26, 52]))
print(sol.sumDigitDifferences(nums=[50, 28, 48]))  # 5
