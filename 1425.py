import heapq


class Solution:
    def constrainedSubsetSum(self, nums: list[int], k: int) -> int:
        """
        整数配列 nums と、整数 k が与えられる。
        その配列の空でない部分列最大の合計を返す。
        その部分列の2つの連続した整数の部分列nums[i] and nums[j]は、k - i <= k を満たす。


        dp[i] に i を選んだ時の最大値を入れていき、最後に dp[:] の最大値をとる。

        - Time complexity: O(n long n)
        - Space complexity: O(n)

        #DP

        Args:
            nums (list[int]): 整数配列 nums
            k (int): 整数 k

        Returns:
            int: 配列 nums の空でない部分列最大の合計を返す
        """
        # print(f"\nnums={nums}")
        dp: list[int] = [0] * len(nums)
        q: list[tuple[int, int]] = []
        heapq.heapify(q)
        for i in range(0, len(nums)):
            # print(f"i={i}, {i - k - 1}")
            # for j in range(i - 1, max(i - k - 1, -1), -1):
            #     # print(f"j={j}, nums[j]={dp[j]}")
            #     dp[i] = max(dp[i], nums[i] + dp[j])
            # print(f"i={i}, q={q}, dp={dp}")
            dp[i] = max(nums[i], nums[i] + (-q[0][0] if q else 0))
            # print(f"dp[i]={dp[i]}")

            while q and q[0][1] <= i - k:
                heapq.heappop(q)

            heapq.heappush(q, (-dp[i], i))

            # print(f"2: dp={-q[0][0] if q else -1}")

        # print(f"dp={dp}")
        return max(dp)


sol = Solution()
print(sol.constrainedSubsetSum(nums=[10, 2, -10, 5, 20], k=2))
print(sol.constrainedSubsetSum(nums=[-1, -2, -3], k=1))
print(sol.constrainedSubsetSum(nums=[10, -2, -10, -5, 20], k=2))
