class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """
        渡されたヒストグラムのバーの高さの配列から、各バーの幅を1として、
        最大の面積を返します。

        横の範囲の全パターンは、n^2 通り存在し、全通り試すと O(n^2) かかる。
        面積というのは、ある横の範囲の面積は、幅掛ける最小の高さとなる。
        そのため、ヒストグラムそれぞれの高さを基準とし、
        それの前の最も近い小さい値 (Nearest Smaller to Left: NSL) がある位置と、
        とそれより後の最も近い小さな値 (Nearest Smaller to Right: NSR) がある位置を
        O(1) で見つけるということができれば、それを元に幅と面積を全体で O(n) で求めることができる。

        その場合、単調増加スタックを利用することで O(n) で前と後の小さな要素を見つけることができる。

        スタックには、自身の高さと、自身を最小としたの面積を記録します。

        まず、プッシュする際に、それまでの自身の高さ基準に、
        それより前の面積、つまり NSL の一つ前からの幅と掛けたものを設定します。

        ポップする際に、ポップされるされる高さを基準とし、一つ後ろからの面積、
        つまり、NSR の一つ前までの幅とプッシュされる高さを掛けたものと、プッシュ時に求めた前の面積との合計を面積とします。
        これにより、あるバーを基準にした面積が求まるので、その面積がこれまでの最小なら最小の面積を更新します。

        これを最後まで行い、最後に高さ0のバーがあるものとして処理をすると最小の面積がわかるのでそれを返します。

        #Stack
        #MonotonicStack
        #NSL
        #NSR

        Time complexity: O(n)
        Space complexity: O(n)

        Args:
            heights (List[int]): ヒストグラムのバーの高さからなる整数の配列を渡します。

        Returns:
            int: ヒストグラムの最大の面積を返します。
        """

        stack: list[tuple[int, int, int]] = [(-1, 0, 0)]  # (index, heigth, area)
        max_area = 0
        heights.append(0)

        for index, height in enumerate(heights):
            while stack and height < stack[-1][1]:
                i, h, a = stack.pop()
                area = a + h * (index - i - 1)
                # print(f"pop: index={i}, width={index - i - 1}, height={h}, area={area}")
                max_area = max(max_area, area)

            area = height * (index - stack[-1][0])
            # print(
            #     f"push: index={index}, width={index - stack[-1][0]}, height={height}, area={area}"
            # )
            stack.append((index, height, area))

        return max_area


sol = Solution()
print(sol.largestRectangleArea(heights=[2, 1, 5, 6, 2, 3]))
print(sol.largestRectangleArea(heights=[2, 4]))
print(sol.largestRectangleArea(heights=[2, 5, 3, 7, 7, 4]))
print(sol.largestRectangleArea(heights=[1, 2, 3, 4, 5]))
