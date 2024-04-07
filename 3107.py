class Solution:
    def minOperationsToMakeMedianK(self, nums: list[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        median = nums[n // 2]

        lower = 0
        upper = 0

        ans = 0

        if k == median:
            return ans

        for i in nums:
            if median == i:
                continue
            if k < median:
                if i < median:
                    lower += 1
                if k < i < median:
                    ans += i - k
            elif k > median:
                if i > median:
                    upper += 1
                if k > i > median:
                    ans += k - i

        # print(
        #     f"k={k}, nums={nums}, median={median}, lower={lower}, upper={upper}, ans={ans}"
        # )

        # print(f"(n+1)//2-lower={(n+1)//2-lower}")
        # print(f"(n+1)//2-upper={(n+1)//2-upper}")

        m = 0
        if k < median:
            m = (n + 1) // 2 - lower
            if n % 2 == 0:
                m += 1
        elif k > median:
            m = (n + 1) // 2 - upper

        ans += m * abs(k - median)

        return ans


sol = Solution()
print(sol.minOperationsToMakeMedianK(nums=[2, 5, 6, 8, 5], k=4))
print(sol.minOperationsToMakeMedianK(nums=[2, 5, 6, 8, 5], k=7))
print(sol.minOperationsToMakeMedianK(nums=[2, 5, 5, 5, 5], k=7))
print(sol.minOperationsToMakeMedianK(nums=[1, 2, 3, 4, 5, 6], k=4))
print(sol.minOperationsToMakeMedianK(nums=[1, 2, 3, 4, 5, 6], k=5))
print(sol.minOperationsToMakeMedianK(nums=[1, 2, 3, 4, 4, 6], k=5))
print(sol.minOperationsToMakeMedianK(nums=[1, 2, 4, 4, 5, 6], k=5))
print(sol.minOperationsToMakeMedianK(nums=[1, 3, 4, 4, 4, 6], k=3))
print(sol.minOperationsToMakeMedianK(nums=[1], k=1000000000))
