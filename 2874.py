class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        """
        0 から始まる整数配列 nums が与えられる。
        i < j < k となるすべての3つの要素 (i, j, k) の最大値を返す。
        マイナスなら0を返す。
        (i, j, k) の3つの値は、（nums[i]-nums[j])*nums[k]に等しい。

        nums[j] を前から順番に繰り返す。
        i、k は、それぞれ nums[j]の左、右の最大値を取得することが、（nums[i]-nums[j])*nums[k]が最大となる。

        全探索すると O(n^3) となり間に合わないので、事前に各インデックスの左右それぞれの最大値を求めておく。

        - Time complexity: O(n)
        - Space complexity: O(n)

        Args:
            nums (list[int]): 0 から始まる整数配列 nums が与えられる。

        Returns:
            int: (i, j, k) の最大値を返す。
        """
        # print(f"nums={nums}")
        n = len(nums)
        max_left = [0] * n
        max_right = [0] * n
        for i in range(n):
            if i > 0:
                max_left[i] = max(max_left[i - 1], nums[i - 1])
            if n - i - 1 < n - 1:
                max_right[n - i - 1] = max(max_right[n - i], nums[n - i])

        # print(f"max_left={max_left}")
        # print(f"max_right={max_right}")

        ans = 0
        for j in range(1, n - 1):
            ans = max(ans, (max_left[j] - nums[j]) * max_right[j])

        return ans


sol = Solution()
print(sol.maximumTripletValue(nums=[12, 6, 1, 2, 7]))
print(sol.maximumTripletValue(nums=[1, 10, 3, 4, 19]))
print(sol.maximumTripletValue(nums=[1, 2, 3]))
print(sol.maximumTripletValue(nums=[2, 3, 1]))
