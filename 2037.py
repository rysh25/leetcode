class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        """
        1 つの部屋には n の seats と n 人の stdudents がいます。長さ n の配列 seats が与えられます。
        ここで、seats[i] は i 番目の座席の位置です。
        また、長さ n の配列 students も与えられます。ここで、students[j] は j 番目の学生の位置です。

        次の移動は何度でも実行できます。

        - i 番目の stdudents の位置を 1 ずつ増減します。

        2 人の stdudents が同じ席に座らないように、各生徒を座席に移動するのに必要な最小移動回数を返します。

        最初は複数の座席または同じ位置の生徒が存在する可能性があることに注意してください。

        - Time complexity: O(n)
        - Space complexity: O(1)

        #Geedy

        Args:
            seats (list[int]): 座席の位置表す配列
            students (list[int]): 生徒の位置を表す配列

        Returns:
            int: 各生徒を座席に移動するのに必要な最小移動回数を返します。
        """

        n = len(seats)

        seats.sort()
        students.sort()

        ans = 0
        for i in range(n):
            ans += abs(seats[i] - students[i])

        return ans


sol = Solution()
print(sol.minMovesToSeat(seats=[3, 1, 5], students=[2, 7, 4]))
print(sol.minMovesToSeat(seats=[4, 1, 5, 9], students=[1, 3, 2, 6]))
print(sol.minMovesToSeat(seats=[2, 2, 6, 6], students=[1, 3, 2, 6]))
