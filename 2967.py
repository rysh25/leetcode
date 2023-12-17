class Solution:
    def minimumCost(self, nums: list[int]) -> int:
        mean = sum(nums) // len(nums)

        def is_parindromic_number(i: int):
            s = str(i)
            a = (len(s) - 1) // 2
            b = len(s) // 2
            # print(f"s={s}, a={a}, b={b}")

            while 0 <= a and b < len(s):
                # print(f"s[{a}]={s[a]}, s[{b}]={s[b]}")
                if s[a] != s[b]:
                    return False
                a -= 1
                b += 1
            return True

        def calc_cost(i: int):
            ret = 0
            for n in nums:
                ret += abs(n - i)
            # print(f"i={i}, const={ret}")
            return ret

        ans = 10**9 + 1

        for i in range(10**9 + 1):
            parindrome = False
            if is_parindromic_number(mean + i):
                print(f"1: i={i}, mean={mean}, parindromic_number={mean+i}")
                parindrome = True
                ans = min(ans, calc_cost(mean + i))
            if is_parindromic_number(mean + i + 1):
                print(f"2: i={i}, mean={mean}, parindromic_number={mean+i+1}")
                parindrome = True
                ans = min(ans, calc_cost(mean + i + 1))
            if is_parindromic_number(mean - i):
                print(f"3: i={i}, mean={mean}, parindromic_number={mean-i}")
                parindrome = True
                ans = min(ans, calc_cost(mean - i))
            if is_parindromic_number(mean - i + 1):
                print(f"4: i={i}, mean={mean}, parindromic_number={mean-i + 1}")
                parindrome = True
                ans = min(ans, calc_cost(mean - i + 1))

            if parindrome:
                return ans
        return ans


sol = Solution()
# print(sol.minimumCost(nums=[1, 2, 3, 4, 5]))
# print(sol.minimumCost(nums=[10, 12, 13, 14, 15]))
# print(sol.minimumCost(nums=[22, 33, 22, 33, 22]))
print(sol.minimumCost(nums=[101, 102, 105, 108, 124]))  # 35
