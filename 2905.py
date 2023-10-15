class Solution:
    def findIndices(
        self, nums: list[int], indexDifference: int, valueDifference: int
    ) -> list[int]:
        n = len(nums)
        a: list[tuple[int, int]] = []  # (num, index)
        for i in range(n):
            a.append((nums[i], i))

        a.sort()
        # print(f"a={a}")
        for i in range(n):
            j = self.binary_search(a, nums[i], i, indexDifference, valueDifference)
            if j > -1:
                return [i, j]

        return [-1, -1]

    def binary_search(
        self,
        a: list[tuple[int, int]],
        num: int,
        i: int,
        indexDifference: int,
        valueDifference: int,
    ) -> int:
        l, r = i - 1, len(a)
        while r - l > 1:
            m = l + (r - l) // 2
            if (
                abs(a[m][0] - num) >= valueDifference
                and abs(a[m][1] - i) >= indexDifference
            ):
                r = m
            else:
                l = m
        # print(
        #     f"r={r}, indexDifference={indexDifference}, valueDifference={valueDifference}"
        # )
        return a[r][1] if r < len(a) else -1


sol = Solution()
print(sol.findIndices(nums=[5, 1, 4, 1], indexDifference=2, valueDifference=4))
print(sol.findIndices(nums=[2, 1], indexDifference=0, valueDifference=0))
print(sol.findIndices(nums=[1, 2, 3], indexDifference=2, valueDifference=4))
