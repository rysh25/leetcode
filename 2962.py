class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        mx = max(nums)
        n = len(nums)
        # print(f"nums={nums}, k={k}, mx={mx}, n={n}")
        freq = 0
        first_index = -1

        ans = 0
        for i in range(len(nums)):
            # print(f"nums[{i}]={nums[i]}")
            if nums[i] == mx:
                freq += 1
                # print(f"freq={freq}")
                if freq == 1:
                    first_index = i
                if freq == k:
                    next_index = i + 1
                    while next_index < n and nums[next_index] != mx:
                        next_index += 1
                    v = (first_index + 1) * (next_index - i)
                    # print(
                    #     f"i={i}, first_index={first_index}, next_index={next_index}, v={v}"
                    # )
                    ans += v
                    # print(f"ans={ans}")

                    first_index += 1
                    while first_index < n and nums[first_index] != mx:
                        first_index += 1
                    freq -= 1
                    # print(f"first_index={first_index}, freq={freq}")
        return ans


sol = Solution()
print(sol.countSubarrays(nums=[1, 3, 2, 3, 3], k=2))
print(sol.countSubarrays(nums=[1, 4, 2, 1], k=3))
print(
    sol.countSubarrays(
        nums=[
            61,
            23,
            38,
            23,
            56,
            40,
            82,
            56,
            82,
            82,
            82,
            70,
            8,
            69,
            8,
            7,
            19,
            14,
            58,
            42,
            82,
            10,
            82,
            78,
            15,
            82,
        ],
        k=2,
    )
)  # 224
