class BIT:
    def __init__(self, n: int):
        self.n = n + 1
        self.bit = [0] * self.n

    def add(self, i: int, x: int):
        while i < self.n:
            self.bit[i] += x
            i += i & -i

    def sum(self, i: int):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def count(self, i: int, x: int):
        l = i + 1
        r = self.n
        count = 0
        while l < r:
            m = (l + r) // 2
            if self.sum(m) > x:
                r = m
            else:
                count += self.sum(m) - self.sum(i)
                l = m + 1
        return count


class Solution:
    def resultArray(self, nums: list[int]) -> list[int]:
        print(f"nums={nums}")
        n = len(nums)
        arr1: list[int] = [nums[0]]
        arr2: list[int] = [nums[1]]

        bit1 = BIT(max(nums))
        bit2 = BIT(max(nums))

        bit1.add(0, nums[0])
        bit2.add(0, nums[1])

        for i in range(2, n):
            print(f"nums[{i}]={nums[i]}")
            c1 = bit1.count(0, nums[i])
            c2 = bit2.count(0, nums[i])

            print(f"c1={c1}, c2={c2}")

            if c1 > c2:
                bit1.add(len(arr1), nums[i])
                arr1.append(nums[i])
            elif c1 < c2:
                bit2.add(len(arr2), nums[i])
                arr2.append(nums[i])
            else:
                print(f"3: len(arr1)={len(arr1)}, len(arr2)={len(arr2)}")
                if len(arr1) <= len(arr2):
                    print(f"3-1")
                    bit1.add(len(arr1), nums[i])
                    arr1.append(nums[i])
                else:
                    print(f"3-2")
                    bit2.add(len(arr2), nums[i])
                    arr2.append(nums[i])

        return [*arr1, *arr2]


sol = Solution()
# print(sol.resultArray(nums=[2, 1, 3, 3]))
# print(sol.resultArray(nums=[5, 14, 3, 1, 2]))
# print(sol.resultArray(nums=[3, 3, 3, 3]))
print(sol.resultArray(nums=[2, 38, 2]))  # [2,38,2]
