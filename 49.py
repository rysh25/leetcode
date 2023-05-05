import collections
from typing import DefaultDict, List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans: DefaultDict[str, List[str]] = collections.defaultdict(list)
        for s in strs:
            sorted_wrod = "".join(sorted(s))
            ans[sorted_wrod].append(s)
        return list(ans.values())


sol = Solution()
print(sol.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
