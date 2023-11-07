class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        """
        n 人のモンスターのグループから都市を守るビデオ ゲームをプレイしています。
        サイズ n の 0 から始まる整数配列 dist が与えられます。ここで、dist[i] は都市から i 番目のモンスターまでの初期距離 (キロメートル単位) です。

        怪物たちは一定の速度で街に向かって歩いていきます。
        各モンスターの速度は、サイズ n の整数配列 speed で指定されます。ここで、speed[i] は、i 番目のモンスターの速度 (キロメートル/分) です。

        完全にチャージすると単一のモンスターを排除できる武器を持っています。
        ただし、武器のチャージには 1 分かかります。
        武器は最初からフルチャージされています。

        モンスターがあなたの街に到達すると負けになります。
        武器が完全にチャージされた瞬間にモンスターが街に到着した場合、
        それは損失としてカウントされ、武器を使用する前にゲームが終了します。

        負ける前に排除できるモンスターの最大数を返します。
        都市に到達する前にすべてのモンスターを排除できる場合は n を返します。


        まずすべてのモンスターについて、何分後に街に到着するかを求め、昇順にソートする。
        到着する時間は、距離/スピードの小数点以下切り上げとする。

        モンスターの到着時間の配列を前から順番に見ていく。
        1つ前との差分を計算し、排除可能な状態かを確認する。

        - Time complexity: O(n log n)
        - Space complexity: O(n)

        Args:
            dist (list[int]): 都市から i 番目のモンスターまでの初期距離 (キロメートル単位) を表す整数配列
            speed (list[int]): 各モンスターの速度を表す整数配列

        Returns:
            int: 負ける前に排除できるモンスターの最大数を返します。
        """
        n = len(dist)

        arrives: list[int] = [0] * n
        for i in range(n):
            arrives[i] = (dist[i] + speed[i] - 1) // speed[i]
        arrives.sort()

        ability_eliminate = 1
        ans = 0
        prev = 0
        for i in range(n):
            ability_eliminate += arrives[i] - prev - 1
            # print(
            #     f"arrives[{i}]={arrives[i]}, prev={prev}, ability_eliminate={ability_eliminate}"
            # )
            if ability_eliminate == 0:
                return ans

            prev = arrives[i]
            ans += 1

        return ans


sol = Solution()
print(sol.eliminateMaximum(dist=[1, 3, 4], speed=[1, 1, 1]))
print(sol.eliminateMaximum(dist=[1, 1, 2, 3], speed=[1, 1, 1, 1]))
print(sol.eliminateMaximum(dist=[3, 2, 4], speed=[5, 3, 2]))
