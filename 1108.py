class Solution:
    def defangIPaddr(self, address: str) -> str:
        """
        指定された IP アドレスの 「.」 を「[.]」に置換して返します。

        Time complexity: O(n)
        Space complexity: O(n)

        Args:
            address (str): IP アドレス文字列を指定します。

        Returns:
            str: 置換した IP アドレス文字列を返します。
        """

        return address.replace(".", "[.]")


sol = Solution()
print(sol.defangIPaddr(address="1.1.1.1"))
