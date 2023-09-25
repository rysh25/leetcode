class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        """
        2-9 の数字を含む文字列が与えられる。
        その数字が表すことができるすべての文字の組み合わせを返す。

        - Time complexity: O(4^n)
        - Space complexity: O(n)

        #Backgrack

        Args:
            digits (str): 2-9 の数字を含む文字列が与えられる。

        Returns:
            list[str]: その数字が表すことができるすべての文字の組み合わせを返す。
        """
        ans: list[str] = []

        digits_letters: list[str] = [
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "qprs",
            "tuv",
            "wxyz",
        ]

        if digits == "":
            return ans

        def backtrack(i: int, curr: str):
            if i == len(digits):
                ans.append(curr[:])
                return
            # print(f"curr={curr}")
            for letter in digits_letters[int(digits[i]) - 2]:
                # print(f"letter={letter}")
                curr += letter

                backtrack(i + 1, curr)

                curr = curr[:-1]

        backtrack(0, "")

        return ans


sol = Solution()
print(sol.letterCombinations(digits="23"))
print(sol.letterCombinations(digits=""))
print(sol.letterCombinations(digits="2"))
