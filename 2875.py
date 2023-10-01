class Solution:
    def minSizeSubarray(self, nums: list[int], target: int) -> int:
        """
        0 から始まる整数配列 nums と、整数 target が与えられる。
        0 から始まるインデックスの配列finity_nums は、nums の要素をそれ自体に無限に追加することによって生成される。
        合計がtargetに等しい infinite_nums の最短の部分配列の長さを返す。
        存在しない場合は、-1 を返す。

        target が nums の合計より大きい場合は、その分は nums の繰り返しになる。
        target から、繰り返し分を引くことと、繰り返しの回数を覚えておく。

        Sliding Window で、n * 2 まで、target の合計が見つかるか確認する。
        見つかったら、r-l とあらかじめ覚えておいた繰り返し分の長さを足したものを返す。
        見つからなければ -1 を返す。

        - Time complexity: O(n)
        - Space complexity: O(1)

        #SlidingWindow

        Args:
            nums (list[int]): 整数配列 nums が与えられる。
            target (int): 整数 target が与えられる。

        Returns:
            int: 合計がtargetに等しい infinite_nums の最短の部分配列の長さを返す。
        """

        # print(f"nums={nums}, target={target}")
        n = len(nums)
        INF = 1001001001
        l = 0
        r = 0
        current_sum = 0
        min_length = INF
        sum_all = sum(nums)
        repeat_length = target // sum_all * n
        target = target % sum_all

        while l <= r and r < n * 2:
            # print(f"current_sum={current_sum}")
            if current_sum == target:
                # print(f"current_sum={current_sum}, r={r}, l={l}, r-l={r-l}")
                min_length = min(r - l, min_length)

            if current_sum >= target:
                # print(f"l++")
                current_sum -= nums[l % n]
                l += 1
            else:
                # print(f"r++")
                current_sum += nums[r % n]
                r += 1

        return min_length + repeat_length if min_length != INF else -1


sol = Solution()
print(sol.minSizeSubarray(nums=[1, 2, 3], target=5))
print(sol.minSizeSubarray(nums=[1, 1, 1, 2, 3], target=4))
print(sol.minSizeSubarray(nums=[2, 4, 6, 8], target=3))
print(sol.minSizeSubarray(nums=[1, 1, 1, 2, 3], target=4))  # 2
# print(sol.minSizeSubarray(nums=[8, 4, 12, 15, 1, 15, 13, 10, 8], target=100))
