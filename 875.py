class Solution:
    def estimateHoursFinishEating(self, piles: list[int], k: int) -> int:
        hours = 0
        if not k:
            return 1001001001

        for pile in piles:
            hours += (pile + k - 1) // k

        # print(f"k={k}, hours={hours}")
        return hours

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        """
        n 房のバナナを表す配列 piles を渡します。i 番目の房は、piles[i] 本のバナナを持ちます。
        h 時間後に、警備員が戻ります。
        Koko は1時間ごとに何本のバナナを食べるか決めることができます。
        Koko は、1時間ごとに1房選んで k 本バナナを食べます。
        選んだふさが k 本以下なら、それ以上食べません。

        警備員が戻るまでに食べ終えることができる最小の k を求めて返します。

        #BinarySearch

        Time complexity: O(n log n)
        Space complexity: O(1)

        Args:
            piles (list[int]): n 房のバナナを表す配列 piles を渡します。
            h (int): 何時間後に警備員が戻るかを指定します。

        Returns:
            int: 警備員が戻るまでに、食べ終わることができる最初の k を返します。
        """

        piles.sort()

        left, right = -1, max(piles) + 1
        while right - left > 1:
            mid = left + (right - left) // 2
            # print(f"h={h}, left={left}, right={right}, mid={mid}")
            if self.estimateHoursFinishEating(piles, mid) <= h:
                right = mid
            else:
                left = mid

        return right


sol = Solution()
print(sol.minEatingSpeed(piles=[3, 6, 7, 11], h=8))
print(sol.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=5))
print(sol.minEatingSpeed(piles=[30, 11, 23, 4, 20], h=6))
