from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        文字列の配列 strs が与えられる。アナグラムをグループにまとめて、任意の順番に返す。

        アナグラムグループを管理するためのディクショナリーを用意する
        文字列でループしながら、ソートした文字列をキーとして、取得したリストに文字列を追加する
        ループが終わった後、ディクショナリーないの全値をリストにして返却する。

        Time complexity: O(n * k log k)
        Space complexixty: O(nk)
            n=the size of strs, k=the average size of string in strs

        #Array
        """
        ans: defaultdict[str, list[str]] = defaultdict(list)
        for s in strs:
            sorted_wrod = "".join(sorted(s))
            ans[sorted_wrod].append(s)
        return list(ans.values())


sol = Solution()
print(sol.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
