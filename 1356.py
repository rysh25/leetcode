class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        """
        整数配列が与えられる。
        ビット表現で1の数の昇順で並べ替える。
        同じ整数が複数場合は、昇順で並べ替える。

        - Time complexity: O(n)
        - Space complexity: O(n)

        Args:
            arr (list[int]): 整数配列

        Returns:
            list[int]: ビット表現で1の数の昇順で並べ替える
        """

        ans: list[tuple[int, int]] = []  # # of 1's, integer
        for a in arr:
            ans.append((bin(a).count("1"), a))

        ans.sort()

        return [a[1] for a in ans]


sol = Solution()
print(sol.sortByBits(arr=[0, 1, 2, 3, 4, 5, 6, 7, 8]))
print(sol.sortByBits(arr=[1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))
