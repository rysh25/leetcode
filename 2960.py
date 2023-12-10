class Solution:
    def countTestedDevices(self, batteryPercentages: list[int]) -> int:
        ans = 0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] - ans > 0:
                ans += 1

        return ans


sol = Solution()
print(sol.countTestedDevices(batteryPercentages=[1, 1, 2, 1, 3]))
print(sol.countTestedDevices(batteryPercentages=[0, 1, 2]))
