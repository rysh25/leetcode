class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        """
        整数は、数値内の各桁が前の桁より 1 つ多い場合に限り、連続した桁になります。

        [low, hight] の範囲内で連続した数字を持つすべての整数の並べ替えられたリストを返します。


        1から9まで順番に、その数値から始まる前の桁より1多い数値を生成する。
        その数値が [low, hight] の範囲内であれば、配列に追加する。

        Args:
            low (int): 範囲の最小
            high (int): 範囲の最大

        Returns:
            list[int]: 連続した数字を持つすべての整数の並べ替えられたリストを返します。
        """
        a: list[int] = []

        for i in range(1, 10):
            num = i
            next_digit = i + 1
            # print(f"!!!!num={num}, next_digit={next_digit}")

            while num <= high and next_digit <= 9:
                num = num * 10 + next_digit
                # print(f"num={num}, next_digit={next_digit}")
                if low <= num <= high:
                    a.append(num)
                next_digit += 1

        a.sort()
        return a


sol = Solution()
print(sol.sequentialDigits(low=100, high=300))
print(sol.sequentialDigits(low=1000, high=13000))
