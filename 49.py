import collections
from typing import DefaultDict, List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        アナグラムグループを管理するためのディクショナリーを用意する
        文字列でループしながら、ソートした文字列をキーとして、取得したリストに文字列を追加する
        ループが終わった後、ディクショナリーないの全値をリストにして返却する。

        Time complexity: O(m * n log n)
            m=the size of strs, n=the average size of string in strs
        Space complexixty: O(n)
        """
        ans: DefaultDict[str, List[str]] = collections.defaultdict(list)
        for s in strs:
            sorted_wrod = "".join(sorted(s))
            ans[sorted_wrod].append(s)
        return list(ans.values())


sol = Solution()
print(sol.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
