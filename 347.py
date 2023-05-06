import heapq
from collections import defaultdict
from typing import DefaultDict, List, Tuple


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        ディクショナリーを使って、各数字の出現回数を計算する
        優先度付きキューに出現回数をプッシュする
        優先度付きキューから、多い順に先頭k個取り出して、リストに追加する
        リストを返す

        Time complexity: O(n log n + k long n)
        Space complexity: O(n)
        """

        d: DefaultDict[int, int] = defaultdict(int)
        for num in nums:
            d[num] += 1

        q: List[Tuple[int, int]] = []
        heapq.heapify(q)
        for key in d:
            heapq.heappush(q, (d[key] * -1, key))

        ans: List[int] = []
        for i in range(0, len(q)):
            # print(f"i={i}, k={k}")
            if i + 1 > k:
                break
            ans.append(heapq.heappop(q)[1])

        return ans


sol = Solution()
print(sol.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
print(sol.topKFrequent(nums=[1], k=1))
print(sol.topKFrequent(nums=[-1, -1], k=1))
print(sol.topKFrequent(nums=[], k=0))
