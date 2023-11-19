class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        # print("a=" + format(a, f"0{n}b"))
        # print("b=" + format(b, f"0{n}b"))
        # print("x=" + format(x, f"0{n}b"))
        # print(
        #     format(a ^ x, f"0{n}b")
        #     + f" ({a^x})"
        #     + " x "
        #     + format(b ^ x, f"0{n}b")
        #     + f" ({b^x})"
        #     + " = "
        #     + format((a ^ x) * (b ^ x), f"0{n}b")
        #     + f" ({(a ^ x) * (b ^ x)})"
        # )
        if n == 0:
            return 0

        MOD = 10**9 + 7

        def max_product(a: int, b: int, n: int):
            x = 0
            for i in range(n - 1, -1, -1):
                bit = 1 << i
                if i % 2 == 0:
                    if (bit & a) == 0:
                        x |= bit
                else:
                    if (bit & b) == 0:
                        x |= bit
            # print("x=" + format(x, f"0{n}b") + f" ({x})")
            # print(f"max_product={((a ^ x) % MOD) * ((b ^ x) % MOD) % MOD}")

            return ((a ^ x) % MOD) * ((b ^ x) % MOD) % MOD

        return max(max_product(a, b, n), max_product(b, a, n))


sol = Solution()
# print(sol.maximumXorProduct(a=12, b=5, n=4, x=2))
# print(sol.maximumXorProduct(a=6, b=7, n=5, x=24))
# print(sol.maximumXorProduct(a=1, b=6, n=3, x=5))
print(sol.maximumXorProduct(a=0, b=4, n=0))
print(sol.maximumXorProduct(a=0, b=10, n=7))  # 14875
