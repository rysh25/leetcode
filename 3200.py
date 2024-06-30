class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        ans = 0

        for i in range(2):
            r, b = red, blue
            j = 1
            is_red = True if i == 0 else False
            while True:
                # print(f"i={i}, j={j}, r={r}, b={b}, is_red={is_red}")
                if is_red and r >= j:
                    r -= j
                elif not is_red and b >= j:
                    b -= j
                else:
                    break

                is_red = not is_red
                j += 1

            # print(f"j={j}")
            ans = max(ans, j - 1)

        return ans


sol = Solution()
print(sol.maxHeightOfTriangle(red=2, blue=4))
print(sol.maxHeightOfTriangle(red=2, blue=1))
print(sol.maxHeightOfTriangle(red=1, blue=1))
print(sol.maxHeightOfTriangle(red=10, blue=1))
print(sol.maxHeightOfTriangle(red=3, blue=8))  # 3
