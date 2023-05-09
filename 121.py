from typing import List


class Solution_sw:
    def maxProfit(self, prices: List[int]) -> int:
        """
        尺取り法 (Sliding Window) を使い、株の売買の利益が一番高くなるタイミングをを探します。

        尺取り法のため、左のポインターと右のポインターを用意する
        右のポンターを処理を進めるために利用し、左のポインターを右より前にある最小値を管理するために使う。
        左と右のポインターをそれぞれ0から始め、右が最後に到達するまでループする：
            左と右の価格を比較し、右の方が小さければ、左を右まで進める
            右の価格から左の価格を引いたものを利益とし、これまでの最大利益であれば更新する。
            右を進める

        Time complexity: O(N)
        Space complexity: O(1)

        #SlidingWindow
        """
        right = 0
        left = 0
        profit = 0
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            profit = max(profit, prices[right] - prices[left])
            right += 1
        return profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = 10**18
        profit = 0
        for price in prices:
            lowest = min(lowest, price)
            profit = max(profit, price - lowest)

        return profit


sol = Solution()
print(sol.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
print(sol.maxProfit(prices=[7, 6, 4, 3, 1]))
print(sol.maxProfit(prices=[]))
