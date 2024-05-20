class SegmentTree:
    def __init__(self, parities: list[bool]):
        n = len(parities)
        self.n = n
        self.tree: list[bool] = [False] * (2 * n)
        self.build(parities)

    def build(self, nums: list[bool]) -> None:
        for i in range(self.n):
            self.tree[self.n + i] = nums[i]

        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] and self.tree[2 * i + 1]

    def query(self, left: int, right: int) -> bool:
        left += self.n
        right += self.n
        res = True
        while left <= right:
            if left % 2 == 1:
                res = res and self.tree[left]
                left += 1
            if right % 2 == 0:
                res = res and self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return res


class Solution:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        pairties: list[bool] = []
        for i in range(len(nums) - 1):
            pairties.append(nums[i] % 2 != nums[i + 1] % 2)

        seg_tree = SegmentTree(pairties)

        result: list[bool] = []
        for from_idx, to_idx in queries:
            if to_idx == from_idx:
                result.append(True)
            else:
                result.append(seg_tree.query(from_idx, to_idx - 1))
        return result


sol = Solution()
print(sol.isArraySpecial(nums=[3, 4, 1, 2, 6], queries=[[0, 4]]))
print(sol.isArraySpecial(nums=[4, 3, 1, 6], queries=[[0, 2], [2, 3]]))
print(sol.isArraySpecial(nums=[4, 3, 1, 6, 7, 8, 8], queries=[[0, 6], [2, 5]]))
