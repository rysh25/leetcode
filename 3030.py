class Solution:
    def resultGrid(self, image: list[list[int]], threshold: int) -> list[list[int]]:

        print(f"image={image}")

        n = len(image)
        m = len(image[0])

        self.result: list[list[int]] = [[-1] * m for _ in range(n)]

        print(f"result={self.result}")

        def expand_region(x: int, y: int):
            if x == 0 or x == n - 1:
                return
            elif y == 0 or y == m -1:
                return

            sub = 1

            while True:
            return 0


sol = Solution()
print(
    sol.resultGrid(
        image=[[10, 20, 30], [15, 25, 35], [20, 30, 40], [25, 35, 45]], threshold=12
    )
)
print(sol.resultGrid(image=[[5, 6, 7], [8, 9, 10], [11, 12, 13]], threshold=1))
