from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        # print(f"nums={nums}, k={k}")
        n = len(nums)
        freq: defaultdict[int, int] = defaultdict(int)

        l, r = 0, 0
        over_k_num = 0
        ans = 0
        while r < n:
            while r < n and freq[nums[r]] < k:
                freq[nums[r]] += 1
                # print(
                #     f"l={l}, r={r}, nums[r]={nums[r]}, freq[nums[r]]={freq[nums[r]] }, r-l-1={r-l}"
                # )
                r += 1
            # print(f"l={l}, r={r},r-l={r - l}, over_k_num={over_k_num}")
            ans = max(ans, r - l)
            if r == n:
                break
            over_k_num = nums[r]

            while l < n:
                freq[nums[l]] -= 1

                # print(
                #     f"l={l}, r={r}, nums[l]={nums[l]}, freq[nums[l]]={freq[nums[l]] }, r-l-1={r-l}"
                # )
                b = False
                if nums[l] == over_k_num:
                    b = True
                l += 1
                if b:
                    break
        return ans


sol = Solution()
print(sol.maxSubarrayLength(nums=[1, 2, 3, 1, 2, 3, 1, 2], k=2))
print(sol.maxSubarrayLength(nums=[1, 2, 1, 2, 1, 2, 1, 2], k=1))
print(sol.maxSubarrayLength(nums=[5, 5, 5, 5, 5, 5, 5], k=4))
print(sol.maxSubarrayLength(nums=[1], k=1))  # 1
print(sol.maxSubarrayLength(nums=[1, 2, 1, 5], k=1))  # 3
