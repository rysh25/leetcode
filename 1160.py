from collections import defaultdict


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        """
        文字列の配列 word と文字列 chars が与えられます。

        文字列は、char からの文字で形成できれば good です (各文字は 1 回のみ使用できます)。

        words 内のすべての good な文字列の長さの合計を返します。

        - Time complexity: O(n*m) # m is sum of the lengths of each string in words
        - Space complexity: O(l)   # l is length of chars

        Args:
            words (list[str]): 文字列の配列
            chars (str): 文字列

        Returns:
            int: words 内のすべての good な文字列の長さの合計を返します。
        """
        freq: defaultdict[str, int] = defaultdict(int)
        for c in chars:
            freq[c] += 1

        ans = 0
        for word in words:
            w = freq.copy()
            good = True
            for c in word:
                if c in w and w[c] > 0:
                    w[c] -= 1
                else:
                    good = False
                    break
            if not good:
                continue

            ans += len(word)
        return ans


sol = Solution()
print(sol.countCharacters(words=["cat", "bt", "hat", "tree"], chars="atach"))
print(sol.countCharacters(words=["hello", "world", "leetcode"], chars="welldonehoneyr"))
