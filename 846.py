class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        """
        アリスはある程度の数のカードを持っており、各グループのサイズが groupSize になり、groupSize の連続するカードで構成されるように、カードをグループに再配置したいと考えています。

        hand[i] が i 番目のカードに書き込まれた値である整数配列 hand と整数の groupSize を指定すると、カードを再配置することができる場合は true を返し、そうでない場合は false を返します。

        - Time complexity: O(n)
        - Space complexity: O(1)

        Args:
            hand (list[int]): hand[i] が i 番目のカードに書き込まれた値である整数配列
            groupSize (int): 整数

        Returns:
            bool: カードを再配置することができる場合は true を返し、そうでない場合は false を返します。
        """

        n = len(hand)

        if n % groupSize != 0:
            return False

        last: list[int] = [-1] * (n // groupSize)
        counts: list[int] = [0] * (n // groupSize)

        # rearranged: list[list[int]] = [[] for _ in range(n // groupSize)]

        hand.sort()

        for h in hand:
            appended = False
            for i in range(n // groupSize):
                if counts[i] > 0 and counts[i] < groupSize and last[i] == h - 1:
                    appended = True
                    last[i] = h
                    counts[i] += 1
                    # rearranged[i].append(h)
                    break

            if not appended:
                for i in range(n // groupSize):
                    if counts[i] == 0:
                        appended = True
                        last[i] = h
                        counts[i] += 1
                        # rearranged[i].append(h)
                        break

            if not appended:
                return False

        # for r in rearranged:
        #     print(f"r={r}")

        return True


sol = Solution()
print(sol.isNStraightHand(hand=[1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize=3))
print(sol.isNStraightHand(hand=[1, 2, 3, 4, 5], groupSize=4))
print(
    sol.isNStraightHand(
        hand=[
            9,
            13,
            15,
            23,
            22,
            25,
            4,
            4,
            29,
            15,
            8,
            23,
            12,
            19,
            24,
            17,
            18,
            11,
            22,
            24,
            17,
            17,
            10,
            23,
            21,
            18,
            14,
            18,
            7,
            6,
            3,
            6,
            19,
            11,
            16,
            11,
            12,
            13,
            8,
            26,
            17,
            20,
            13,
            19,
            22,
            21,
            27,
            9,
            20,
            15,
            20,
            27,
            8,
            13,
            25,
            23,
            22,
            15,
            9,
            14,
            20,
            10,
            6,
            5,
            14,
            12,
            7,
            16,
            21,
            18,
            21,
            24,
            23,
            10,
            21,
            16,
            18,
            16,
            18,
            5,
            20,
            19,
            20,
            10,
            14,
            26,
            2,
            9,
            19,
            12,
            28,
            17,
            5,
            7,
            25,
            22,
            16,
            17,
            21,
            11,
        ],
        groupSize=10,
    )
)
