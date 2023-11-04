from collections import deque


class Solution:
    def minIncrementOperations(self, nums: list[int], k: int) -> int:
        # print(f"nums={nums}, k={k}")
        n = len(nums)
        INF = 10 * 9 + 1
        ans = 0
        l, r = 0, 0
        count_less_k = 0
        range_array: deque[int] = deque()
        while r < n:
            while r - l < 3:
                range_array.append(nums[r])
                count_less_k += 1 if nums[r] < k else 0
                r += 1

            if count_less_k == 3:
                print(f"count_less_k == 3: range_array={range_array}")
                i = 0
                if r < n:
                    for i in range(r, min(r + 3, n)):
                        if nums[i] > k:
                            break
                        range_array.append(nums[i])

                mn = INF
                mn_index = -1
                if len(range_array) == 5:
                    print(f"5: range_array={range_array}")
                    if k - range_array[2] < mn:
                        mn = k - range_array[2]
                        mn_index = 2
                    if k - range_array[1] + k - range_array[4] < mn:
                        mn = k - range_array[1] + k - range_array[4]
                        mn_index = 1
                if len(range_array) >= 4:
                    print(f"4: range_array={range_array}")
                    if k - range_array[0] + k - range_array[3] < mn:
                        mn = k - range_array[0] + k - range_array[3]
                        mn_index = 0

                    ans += k - range_array[mn_index]
                    range_array[mn_index] = k
                else:
                    print(f"else:")
                    mx = max(range_array)
                    for i in range(len(range_array) - 1, -1, -1):
                        if range_array[i] == mx:
                            range_array[i] = k
                    ans += k - mx
                count_less_k = 2

            num = range_array.popleft()
            if num < k:
                count_less_k -= 1
            l += 1
        return ans


sol = Solution()
# print(sol.minIncrementOperations(nums=[2, 3, 0, 0, 2], k=4))
print(sol.minIncrementOperations(nums=[0, 1, 3, 3], k=5))
# print(sol.minIncrementOperations(nums=[1, 1, 2], k=1))
# print(sol.minIncrementOperations(nums=[43, 31, 14, 4], k=73))  # 42
