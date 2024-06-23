class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        from collections import defaultdict

        n = len(power)
        counts: defaultdict[int, int] = defaultdict(int)
        for i in range(n):
            counts[power[i]] += 1

        keys = list(counts.keys())
        keys.sort()

        dp = [0] * (len(keys) + 1)

        mx = 0
        # print(f"keys={keys}")
        for k in range(len(keys)):
            # print(f"keys[{k}]={keys[k]}, counts[k]={counts[keys[k]]}")
            dp[k] = keys[k] * counts[keys[k]]

            # print(f"dp[k]={dp[k]}")
            for i in range(k - 1, max(k - 4, -1), -1):
                if keys[i] < keys[k] - 2:
                    # print(f"keys={keys[i]}")
                    mx = max(mx, dp[i])

            dp[k] += mx

            # print(f"dp[{k}]={dp[k]}, mx={mx}")

        return max(dp)


sol = Solution()
print(sol.maximumTotalDamage(power=[1, 1, 3, 4]))
print(sol.maximumTotalDamage(power=[7, 1, 6, 6]))
print(sol.maximumTotalDamage(power=[5, 9, 2, 10, 2, 7, 10, 9, 3, 8]))  # 31
print(sol.maximumTotalDamage(power=[3, 4, 8, 10, 8, 8, 3]))  # 30
