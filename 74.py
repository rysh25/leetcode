from typing import List, Tuple


def bin_search(matrix: List[List[int]], target: int) -> Tuple[int, int]:
    print(f"matrix={matrix}, target={target}")
    rows = len(matrix)
    if rows == 0:
        return (-1, -1)
    cols = len(matrix[0])
    fail, ok = -1, rows
    m = -1
    while ok - fail > 1:
        m = fail + (ok - fail) // 2
        # print(f"fail={fail}, ok={ok}, m={m}")
        if target <= matrix[m][-1]:
            ok = m
        elif target > matrix[m][-1]:
            fail = m

    if ok >= rows:
        return (-1, -1)

    row = ok

    fail, ok = -1, cols

    while ok - fail > 1:
        m = fail + (ok - fail) // 2
        print(f"fail={fail}, ok={ok}, m={m}, row={row}")
        if target == matrix[row][m]:
            return (row, m)
        elif target < matrix[row][m]:
            ok = m
        else:
            fail = m

    return (-1, -1)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        2分探索を行います。
        初めに、行の2分探索を行う。
        target が各行の最終列以下なら、OK に mid を設定する。(現在の行以上に存在する。)
        target が各行の最終列より上なら、fail に mid を設定する。(現在の行より下には存在しない。)
        OK が行数以上なら、見つからなかったとする。
        次に、見つかった行の、列に対し2分探索を実施する。
        見つかったら True を返し、見つからなかったら False を返す。

        Time complexity: O(log N)
        Space complexity: O(1)
        """
        return bin_search(matrix, target) != (-1, -1)


sol = Solution()
print(
    sol.searchMatrix(
        matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3
    )
)
print(
    sol.searchMatrix(
        matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13
    )
)
print(sol.searchMatrix(matrix=[[1, 1]], target=2))
print(sol.searchMatrix(matrix=[[1, 3]], target=3))
print(sol.searchMatrix(matrix=[[1], [3], [5]], target=3))
