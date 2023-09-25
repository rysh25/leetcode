class Solution:
    def partition(self, s: str) -> list[list[str]]:
        """
        文字列 s が渡される。
        s を各区分のすべての部分文字列が回文区切って返します。

        バックトラック法で、すべての文字列の組み合わせを回文かどうか判定し、
        回文であれば結果用のリストに追加します。

        - Time complexity: O(n * 2^n)
        - Space complexity: O(n)

        #Backgrack

        Args:
            s (str): 文字列が渡されます。

        Returns:
            list[list[str]]: すべてが回文となる部分文字列のリストを返します。
        """
        ans: list[list[str]] = []

        def backtrack(i: int, curr: list[str]):
            if i == len(s):
                ans.append(curr[:])
                return

            for j in range(i, len(s)):
                wk = s[i : j + 1]
                if not self.isPalindrome(wk):
                    continue
                # print(f"i={i}, j={j}, wk={wk}")
                curr.append(wk)
                backtrack(j + 1, curr)
                curr.pop()
                # poped = curr.pop()
                # print(f"i={i}, j={j}, poped={poped}")

        backtrack(0, [])
        return ans

    def isPalindrome(self, s: str):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


sol = Solution()
print(sol.partition(s="aab"))
print(sol.partition(s="a"))
