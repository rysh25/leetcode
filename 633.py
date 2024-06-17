class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        非負整数 c が与えられます。
        a2 + b2 = c となる 2 つの整数 a および b があるかどうかを判断します。


        はじめに、low = 0、と high = sqrt(c) 以上で、初期化する
        low * low + high * high が c 以内になる high を見つける
        low * low + high * high = c であれば、True を返す
        low をインクリメントし、繰り返す。
        low をインクリメントした場合、high は、前回より必ず小さくなるはず。
        そのため、two pointers で、O(n) で検索できる。

        - Time complexity: O(n)
        - Space complexity: O(1)

        #TowPointers

        Args:
            c (int): 非負整数

        Returns:
            bool: a2 + b2 = c となる 2 つの整数 a および b があるかどうかを返します。
        """

        def sqrt(c: int) -> int:
            i = 0
            while i * i <= c:
                if i * i == c:
                    return i
                i += 1

            return i

        low = 0
        high = sqrt(c)

        # print(f"low={low}, high={high}")

        while low <= high:

            while low * low + high * high > c:
                high -= 1

            # print(f"low={low}, high={high}")

            if low * low + high * high == c:
                return True

            low += 1

        return False


sol = Solution()
print(sol.judgeSquareSum(c=5))
print(sol.judgeSquareSum(c=3))
