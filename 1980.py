class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        """
        それぞれ長さが n 個の一意のバイナリ文字列の配列 nums が与えられます。
        nums に現れない長さ n のバイナリ文字列を返します。

        複数の回答がある場合は、どれを返しても構いません。


        nums ないのバイナリ文字列を数値に変換して set に入れる。
        0 から n^2 までの数値のうち、set を確認し、nums に存在しない数値ならバイナリ文字列にして返す。

        - Time complexity: O(n)
        - Space complexity: O(n)

        Args:
            nums (list[str]): バイナリ文字列の配列

        Returns:
            str: nums に現れない長さ n のバイナリ文字列を返します。
        """
        n = len(nums)
        exists: set[int] = set()
        for i in range(n):
            exists.add(int(nums[i], 2))
        for i in range(2**n):
            if i not in exists:
                return format(i, "0" + str(n) + "b")

        return ""


sol = Solution()
print(sol.findDifferentBinaryString(nums=["01", "10"]))
print(sol.findDifferentBinaryString(nums=["00", "01"]))
print(sol.findDifferentBinaryString(nums=["111", "011", "001"]))
