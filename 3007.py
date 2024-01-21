class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        seq: list[int] = []

        def count_bits(n: int, x: int) -> int:
            binary_representation = bin(n)[2::][::-1]
            # print(
            #     f"n={n}, x={x}, len(binary_representation)={len(binary_representation)} x={x}, binary_representation={binary_representation}"
            # )
            count_of_1s = 0
            for i in range(len(binary_representation) // x):
                c = binary_representation[((i + 1) * x - 1)]
                # print(f"i={i}, c={c}")
                count_of_1s += 1 if c == "1" else 0

            return count_of_1s

        sum = 0
        i = 1
        while sum <= k:
            bits = count_bits(i, x)

            # print(f"i={i}, bits={bits}")

            sum += bits
            seq.append(sum)
            i += 1

        # print(f"seq={seq}")

        return len(seq) - 1


sol = Solution()
print(sol.findMaximumNumber(k=9, x=1))
print(sol.findMaximumNumber(k=7, x=2))
print(sol.findMaximumNumber(k=19, x=6))
