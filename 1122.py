class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        """
        2 つの配列 arr1 と arr2 渡されます。
        arr2 の要素はそれぞれ異なり、arr2 のすべての要素は arr1 にもあります。

        arr1 の要素を並べ替えて、arr1 内の項目の相対的な順序が arr2 と同じになるようにします。
        arr2 に表示されない要素は、arr1 の最後に昇順で配置する必要があります。

        - Time complexity: O(n)
        - Space complexity: O(n)

        #CountingSort

        Args:
            arr1 (list[int]): 配列
            arr2 (list[int]): 配列

        Returns:
            list[int]: 結果を返します。
        """
        from collections import defaultdict

        counts: defaultdict[int, int] = defaultdict(int)

        for a in arr1:
            counts[a] += 1

        ans: list[int] = []

        for a in arr2:
            for _ in range(counts[a]):
                ans.append(a)
            counts[a] = 0

        rest: list[int] = []

        for k in counts:
            if counts[k] > 0:
                for _ in range(counts[k]):
                    rest.append(k)

        rest.sort()
        return ans + rest


sol = Solution()
print(
    sol.relativeSortArray(
        arr1=[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2=[2, 1, 4, 3, 9, 6]
    )
)
print(sol.relativeSortArray(arr1=[28, 6, 22, 8, 44, 17], arr2=[22, 28, 8, 6]))
