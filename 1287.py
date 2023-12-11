from collections import defaultdict


class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        """
        非降順でソートされた整数配列が与えられます。
        配列内に 25% を超える確率で出現する整数が 1 つだけ存在し、その整数を返します。

        - Time complexity: O(n)
        - Space complexity: O(n)

        Args:
            arr (list[int]): 非降順でソートされた整数配列

        Returns:
            int: 25% を超える確率で出現する整数を返します。
        """
        threshold = len(arr) * 0.25
        freq: defaultdict[int, int] = defaultdict(int)
        for i in arr:
            freq[i] += 1
            if freq[i] > threshold:
                return i
        return -1


sol = Solution()
print(sol.findSpecialInteger(arr=[1, 2, 2, 6, 6, 6, 6, 7, 10]))
print(sol.findSpecialInteger(arr=[1, 1]))
