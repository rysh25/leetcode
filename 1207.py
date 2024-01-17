class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        """
        整数の配列 arr を指定すると、配列内の各値の出現数が一意であれば true を返し、それ以外の場合は false を返します。

        - Time complexity: O(n)
        - Space complexity: O(n)

        Args:
            arr (list[int]): 整数の配列

        Returns:
            bool: 配列内の各値の出現数が一意であれば true を返し、それ以外の場合は false を返します。
        """
        from collections import defaultdict

        freq: defaultdict[int, int] = defaultdict(int)
        occur: defaultdict[int, int] = defaultdict(int)

        for a in arr:
            freq[a] += 1

        for k in freq:
            if freq[k] in occur:
                return False
            occur[freq[k]] += 1

        return True


sol = Solution()
print(sol.uniqueOccurrences(arr=[1, 2, 2, 1, 1, 3]))
print(sol.uniqueOccurrences(arr=[1, 2]))
print(sol.uniqueOccurrences(arr=[-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
