class Solution:
    def numberOfSteps(self, num: int) -> int:
        """
        指定された整数を0に減らすステップ数を返します。

        整数なら2で割り、そうでないなら1を引きます。

        - Time complexity: O(log n)
        - Space complexity: O(1)

        Args:
            num (int): 整数を指定します。

        Returns:
            int: 0にするまでにかかったステップ数を返します。
        """

        ans = 0
        while num:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            ans += 1

        return ans


sol = Solution()
print(sol.numberOfSteps(num=14))
print(sol.numberOfSteps(num=8))
print(sol.numberOfSteps(num=123))
