from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        整数の配列から、足すと0になる3つ数値の全ての組みを探して尺取り法 (Two Pointers) 返す。

        数値のみを返せば良いので、この後の処理のため昇順にソートする。
        配列を初めから順番にループする。
        これが組み合わせを探索するための基準の値となる。
        この値と足すと0になる数値を、この数値より後ろからの尺取り法で探していく。
        尺取り法では、左右から基準の値と足して0になるか見て、なったなら値の組を記憶する。
        0より大きければ右を前にずらす
        小さければ左を進める。
        右と左がぶつかったら、基準の値を次の進める。
        全ての基準の値の処理が終わったら、見つけた値の組みの配列を返す。

        Time complexity: O(n^2)
        Space complexity: O(n)

        #TwoPointers
        """
        nums.sort()
        # print(f"nums={nums}")

        ans: List[List[int]] = []

        for i, target in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                # print(f"i={i}, left={left}, right={right}")
                n = target + nums[left] + nums[right]
                if n == 0:
                    ans.append([target, nums[left], nums[right]])
                    right -= 1
                    while True:
                        left += 1
                        if nums[left] != nums[left - 1] or left >= right:
                            break
                elif n > 0:
                    right -= 1
                else:
                    left += 1

        return ans


sol = Solution()
print(sol.threeSum(nums=[-1, 0, 1, 2, -1, -4]))
print(sol.threeSum(nums=[0, 1, 1]))
print(sol.threeSum(nums=[0, 0, 0]))
print(sol.threeSum(nums=[-2, 0, 1, 1, 2]))  # [[-2, 0, 2], [-2, 1, 1]]
print(sol.threeSum(nums=[-2, 0, 0, 2, 2]))  # [[-2,0,2]]
