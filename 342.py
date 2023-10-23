class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """
        整数 n が与えられる。
        nが4の累乗であれば true を返す。そうでなければ false を返す。

        全探索する。
        4^16 は、2^32 のため、15まで試せば良い。

        - Time complexity: O(log n)
        - Space complexity: O(1)

        Args:
            n (int): 整数

        Returns:
            bool: もし4乗なら true を返す。そうでなければ false を返す。
        """
        for i in range(16):
            if 4**i == n:
                return True

        return False


sol = Solution()
print(sol.isPowerOfFour(n=16))
print(sol.isPowerOfFour(n=5))
print(sol.isPowerOfFour(n=1))
print(sol.isPowerOfFour(n=1073741824))
