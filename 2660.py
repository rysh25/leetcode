from typing import List


def cal_score(player: List[int]):
    strike = 0
    score = 0
    for pin in player:
        mul = 1
        if strike > 0:
            mul = 2
            strike -= 1

        score += pin * mul
        # print(f"score={score}")
        if pin == 10:
            strike = 2

    return score


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        p1_score = cal_score(player1)
        p2_score = cal_score(player2)

        # print(f"p1={p1_score}, p2={p2_score}")

        if p1_score > p2_score:
            return 1
        elif p1_score < p2_score:
            return 2
        else:
            return 0


sol = Solution()
print(sol.isWinner(player1=[4, 10, 7, 9], player2=[6, 5, 2, 3]))
print(sol.isWinner(player1=[3, 5, 7, 6], player2=[8, 10, 10, 2]))
print(sol.isWinner(player1=[2, 3], player2=[4, 1]))
print(sol.isWinner(player1=[5, 6, 1, 10], player2=[5, 1, 10, 5]))
