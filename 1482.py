class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        """
        整数配列 bloomDay、整数 m、整数 kが与えられます。

        あなたは m 個の花束を作りたいと思っています。
        花束を作るには、庭から隣接するk個の花を使用する必要があります。

        庭は n 個の花で構成されており、i 番目の花がbloomDay[i]で咲き、正確に1つの花束として使用できます。

        庭から m 個の花束を作ることができるようになるまで待機する必要がある最小日数を返します。
        m 個の花束を作ることが不可能な場合は -1 を返します

        - Time complexity: O(n log n)
        - Space complexity: O(1)

        #BinarySearch

        Args:
            bloomDay (list[int]): 整数配列
            m (int): 整数
            k (int): 整数

        Returns:
            int: 庭から m 個の花束を作ることができるようになるまで待機する必要がある最小日数を返します。
        """
        n = len(bloomDay)

        def calc_bloom(days: int):
            streak = 0

            flowers = 0
            for i in range(n):
                # print(f"i={i}, bloomDay[i]={bloomDay[i]}")
                if bloomDay[i] <= days:
                    streak += 1
                else:
                    streak = 0

                if streak >= k:
                    flowers += 1
                    streak = 0

            # print(f"days={days}, flowers={flowers}, k={k}")
            return flowers

        max_day = max(bloomDay) + 1
        # print(f"max_day={max_day}")
        low, high = -1, max_day

        while high - low > 1:
            mid = low + (high - low) // 2
            # print(f"low={low}, high={high}, m={m}")

            if calc_bloom(mid) >= m:
                high = mid
            else:
                low = mid

        return high if high < max_day else -1


sol = Solution()
print(sol.minDays(bloomDay=[1, 10, 3, 10, 2], m=3, k=1))
print(sol.minDays(bloomDay=[1, 10, 3, 10, 2], m=3, k=2))
print(sol.minDays(bloomDay=[7, 7, 7, 7, 12, 7, 7], m=2, k=3))
