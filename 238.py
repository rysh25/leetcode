from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        数値の配列 nums が与えられる。
        nums の、対応するインデックス以外の数値をかけた結果となる配列を返す。

        計算するための nums と同じ要素数の配列を、各要素1で初期化した配列 ans を用意する。
        前から、積を計算するための変数 prefix を1で初期化する。
        この prefix 変数で、一つ前までの nums の要素をかけた値を管理する
        nums の要素数分前からループする:
            ans[i] に ans[i] * prefix を入れる

        後ろから、積を計算するための変数 suffix を1で初期化する。
        この suffix 変数で、一つ後ろまでの nums の要素をかけた値を管理する
        nums の要素数分後ろからループする:
            ans[i] に ans[i] * suffix を入れる (prefix と suffix をかけた値となる)
            suffix を suffix * nums[i] で更新する

        ans を返す

        Time complexity: O(N)
        Space complexity: O(N)
        """
        ans = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            ans[i] *= prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans


sol = Solution()
print(sol.productExceptSelf(nums=[1, 2, 3, 4]))
print(sol.productExceptSelf([-1, 1, 0, -3, 3]))
