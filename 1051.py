class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        """
        ある学校では、毎年全生徒の写真を撮ろうとしています。生徒は身長の降順ではない順番で一列に並ぶように求められます。
        この順序を整数配列 expected で表すとします。
        ここで、expected[i] は、列に並んでいる i 番目の生徒の予想される身長です。

        学生が立っている現在の順序を表す整数配列 heights が与えられます。各 heights[i] は、列に並んだ i 番目の学生の身長です。

        heights[i] != expected[i] となるインデックスの数を返します。

        - Time complexity: O(n)
        - Space complexity: O(n)

        Args:
            heights (list[int]): 学生が立っている現在の順序を表す整数配列

        Returns:
            int: heights[i] != expected[i] となるインデックスの数を返します。
        """
        n = len(heights)
        expected = sorted(heights)

        ans = 0
        for i in range(n):
            if heights[i] != expected[i]:
                ans += 1

        return ans


sol = Solution()
print(sol.heightChecker(heights=[1, 1, 4, 2, 1, 3]))
print(sol.heightChecker(heights=[5, 1, 2, 3, 4]))
print(sol.heightChecker(heights=[1, 2, 3, 4, 5]))
