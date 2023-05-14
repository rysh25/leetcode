class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        一意の整数配列が指定されます。
        すべての部分集合 (Subset) を返します。

        バックトラッキングで部分集合を作成します。

        - Time complexity: O(2^n)
        - Space complexity: O(n*2^n)

        n は、nums の要素数を表します。

        #BackTracking

        Args:
            nums (list[int]): 一意の整数配列を指定します。

        Returns:
            list[list[int]]: すべての部分集合 (Subset) を返します。順番は任意です。
        """

        ans: list[list[int]] = []
        s: list[int] = []

        def backtrack(i: int = 0):
            if i >= len(nums):
                ans.append(s.copy())
                print(f"i >= len(nums): s={s}")
                return

            s.append(nums[i])
            print(f"Push: i={i}, nums[i]={nums[i]}")
            backtrack(i + 1)

            s.pop()
            print(f"Pop: i={i}, nums[i]={nums[i]}")
            backtrack(i + 1)

        backtrack(0)

        return ans


class Solution_BBF:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        一意の整数配列が指定されます。
        すべての部分集合 (Subset) を返します。

        ビット全探索で部分集合を作成します。

        - Time complexity: O(n*2^n)
        - Space complexity: O(n*2^n)

        n は、nums の要素数を表します。

        #BruteForce
        #BitwiseBruteForce

        Args:
            nums (list[int]): 一意の整数配列を指定します。

        Returns:
            list[list[int]]: すべての部分集合 (Subset) を返します。順番は任意です。
        """

        ans: list[list[int]] = []
        for bit in range(1 << len(nums)):
            ans.append([])
            for i in range(len(nums)):
                if (bit >> i) & 1:
                    ans[bit].append(nums[i])

        return ans


sol = Solution()
print(sol.subsets(nums=[1, 2, 3]))
print(sol.subsets(nums=[0]))
