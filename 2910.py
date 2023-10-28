from collections import defaultdict


class Solution:
    def minGroupsForValidAssignment(self, nums: list[int]) -> int:
        n = len(nums)
        count: defaultdict[int, int] = defaultdict(int)

        for i in range(n):
            count[nums[i]] += 1
        print(f"count={count}")
        freq: list[int] = list(count.values())
        freq.sort()
        print(f"freq={freq}")
        ans = 0

        def count_split(m: int, freq: int) -> int:
            if m >= freq:
                return 1
            if freq % 2 == 0:
                return count_split(m, freq // 2) * 2
            else:
                return count_split(m, freq // 2) + count_split(m, freq // 2 + 1)

        i = len(freq) - 1
        ans = 0
        min_freq = freq[0]
        while 0 <= i:
            split = 1
            if min_freq + 1 < freq[i]:
                # print(f"freq[i]={freq[i]}, split={split}")
                split = (freq[i] + min_freq) // (min_freq + 1)
                freq[i] = freq[i] // split
                if min_freq > freq[i]:
                    i = len(freq) - 1
                    min_freq = freq[i]
                    ans = split
                    continue
            # if freq[0] + 1 < freq[i]:
            #     split = count_split(freq[0] + 1, freq[i])
            print(f"split={split}")
            ans += split
            i -= 1

        return ans


sol = Solution()
# print(sol.minGroupsForValidAssignment(nums=[3, 2, 3, 2, 3]))
# print(sol.minGroupsForValidAssignment(nums=[10, 10, 10, 3, 1, 1]))
# print(sol.minGroupsForValidAssignment(nums=[2, 2, 2, 2, 2, 1, 2]))  # 4
# print(sol.minGroupsForValidAssignment(nums=[1, 2, 3, 3, 3, 3, 3]))  # 5
# print(sol.minGroupsForValidAssignment(nums=[1, 3, 1, 1, 1, 1, 2, 1, 3, 1, 3]))  # 7
# print(sol.minGroupsForValidAssignment(nums=[1, 1, 3, 3, 1, 1, 2, 2, 3, 1, 3, 2]))  # 5
print(
    sol.minGroupsForValidAssignment(nums=[2, 1, 1, 3, 2, 1, 1, 3, 3, 3, 1, 3, 3, 2])
)  # 5
