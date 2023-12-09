class Solution:
    def minimumAddedCoins(self, coins: list[int], target: int) -> int:
        print(f"target={target}")
        coins.sort()

        ans = 0
        current_sum = 1
        for i in range(len(coins)):
            # print(f"1: coins[{i}]={coins[i]}, current_sum={current_sum}")
            if current_sum > target:
                # print(f"1 return: current_sum={current_sum}, target={target}")
                break
            elif coins[i] <= current_sum:
                current_sum += coins[i]
            else:
                # print(f"ans++")
                ans += 1
                current_sum += current_sum

        # print(f"current_sum={current_sum}")

        # while current_sum <= target:
        #     print(f"2: current_sum={current_sum}")
        #     ans += 1
        #     current_sum += current_sum

        return ans


sol = Solution()
print(sol.minimumAddedCoins(coins=[1, 4, 10], target=19))
print(sol.minimumAddedCoins(coins=[1, 4, 10, 5, 7, 19], target=19))
print(sol.minimumAddedCoins(coins=[1, 1, 1], target=20))
