class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        長さnの整数配列 height が与えられる。
        そこには、n本の縦棒があり、高さが i 番目の高さ height[i] となうr。

        最も多くの水を含む x 軸と2本の線を見つける

        水槽に蓄えられる最大の水の量を返します。

        水の面積は次の2つの要因によって決まる
        1. x 軸の長さ
        2. 2つの棒の低い方の高さ

        双方向ポインタ (Two Pointers) を使用して、配列の最初と最後から中心に向かって移動します。
        その際、低い方の進めます。高い方を進めることで、面積が増えることはないですが、引く方法進めることで、
        面積が増える可能性があるためです。

        l, r の2つのポインターを用意する
        l は0からr はlen(height)からスタートすし、それぞれの方向に向けて進めていく
        次の処理をポインターがぶつかるまで進める:
            height[l] と height[r] の低い方を高さとして、面積を求める。
            これまでに求めた面性を超えていたら最大面積を更新する。
            低い方のポインターを進める。

        - Time complexity: O(n)
        - Space complexity: O(1)

        #TwoPointers

        Args:
            height (list[int]): n本の縦棒の高さを表す配列が渡されます。

        Returns:
            int: 水槽に蓄えられる最大の水の量を返します。
        """
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            h = min(height[l], height[r])
            ans = max(h * (r - l), ans)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return ans


sol = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(sol.maxArea(height))
height = [1, 1]
print(sol.maxArea(height))
