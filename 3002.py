from collections import defaultdict


class Solution:
    def maximumSetSize(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        d1: defaultdict[int, int] = defaultdict(int)
        d2: defaultdict[int, int] = defaultdict(int)

        for i in range(n):
            d1[nums1[i]] += 1
            d2[nums2[i]] += 1

        remove1 = n // 2
        remove2 = n // 2

        # print(f"d1={d1}")
        # print(f"d2={d2}")

        for k in d1:
            if d1[k] > 1:
                remove1 -= d1[k] - 1
                d1[k] = 1

        for k in d2:
            if d2[k] > 1:
                remove2 -= d2[k] - 1
                d2[k] = 1

        # print(f"d1={d1}")
        # print(f"d2={d2}")
        # print(f"remove1={remove1}, remove2={remove2}")

        if remove1 > 0:
            for k in d1:
                if d1[k] >= 1 and d2[k] > 0:
                    remove1 -= d1[k]
                    d1[k] = 0

        if remove2 > 0:
            for k in d2:
                if d2[k] >= 1 and d1[k] > 0:
                    remove2 -= d2[k]
                    d2[k] = 0

        # print(f"d1={d1}")
        # print(f"d2={d2}")

        # print(f"remove1={remove1}, remove2={remove2}")

        if remove1 > 0:
            for k in d1:
                if remove1 <= 0:
                    break
                remove1 -= d1[k]
                d1[k] = 0

        # print(f"d1={d1}")

        if remove2 > 0:
            for k in d2:
                if remove2 <= 0:
                    break
                remove2 -= d2[k]
                d2[k] = 0
        # print(f"d2={d2}")
        # print(f"remove1={remove1}, remove2={remove2}")

        st: set[int] = set()
        for k in d1:
            if d1[k] > 0:
                st.add(k)
        for k in d2:
            if d2[k] > 0:
                st.add(k)

        return len(st)


sol = Solution()
print(sol.maximumSetSize(nums1=[1, 2, 1, 2], nums2=[1, 1, 1, 1]))
print(sol.maximumSetSize(nums1=[1, 2, 3, 4, 5, 6], nums2=[2, 3, 2, 3, 2, 3]))
print(sol.maximumSetSize(nums1=[1, 1, 2, 2, 3, 3], nums2=[4, 4, 5, 5, 6, 6]))
print(sol.maximumSetSize(nums1=[1, 2, 1, 1], nums2=[1, 2, 3, 4]))
print(sol.maximumSetSize(nums1=[1, 1, 1, 1], nums2=[12, 23, 41, 9]))  # 3
print(sol.maximumSetSize(nums1=[2, 4, 1, 4], nums2=[10, 2, 4, 10]))  # 4
