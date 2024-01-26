class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        """
        ボールが入った m x n 個のグリッドがあります。
        ボールは最初は [startRow, startColumn] の位置にあります。
        ボールをグリッド内の 4 つの隣接するセルの 1 つに移動することができます (場合によっては、グリッドの境界を越えてグリッドの外に移動することもできます)。 
        最大でも maxMove の動きをボールに適用できます。

        5 つの整数 m、n、maxMove、startRow、startColumn を指定すると、ボールをグリッド境界の外に移動するパスの数を返します。
        答えは非常に大きくなる可能性があるため、10^9 + 7 を法として返します。
        
        
        DP を行う。
        dp[i][j] に [i, j] からグリッド外に行くことができるパスの数を記録する。
        それを 移動1回からmaxMoves 回まで、繰り返す。dp[i][j]には、初期値としてその座標から一回でグリッド外に行くことができるパスの数を持ち、
        そこに、その隣の座標の前回の移動のパス数を足す。
        
        dp[startRow][startColumn] がその座標から maxMove 回の移動で、グリッド外に出るパスの数となる。
        
        
        - Time complexity: O(n * m)
        - Space complexity: O(1)
        
        #DP

        Args:
            m (int): グリッドの列数
            n (int): グリッドの行数
            maxMove (int): ボールの最大移動数
            startRow (int): ボールの最初の行数
            startColumn (int): ボールの最初の列数

        Returns:
            int: ボールをグリッド境界の外に移動するパスの 10^9+7 を法とする数を返す。
        """
        MOD = 10**9 + 7
        count: list[list[int]] = [[0] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                if r == 0:
                    count[r][c] += 1
                if r == m - 1:
                    count[r][c] += 1
                if c == 0 :
                    count[r][c] += 1
                if c == n - 1:
                    count[r][c] += 1
        
        
        # print(f"count={count}")
        
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
            
        dp: list[list[int]] = [[0] * n for _ in range(m)]
                    
        for _ in range(1, maxMove+1):
            tmp: list[list[int]] = [[0] * n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    # print(f"r={r}, c={c}")
                    tmp[r][c] = count[r][c]
                
                    for di in range(4):
                        nr = r + dy[di]
                        nc = c + dx[di]
                        if nr < 0 or nr >= m or nc < 0 or nc >= n:
                            continue
                        # print(f"nr={nr}, nc={nc}")
                        tmp[r][c] += dp[nr][nc] % MOD
            dp = tmp
            # print(f"dp={dp}")
        return dp[startRow][startColumn] % MOD
            
        
    
sol = Solution()
print(sol.findPaths(m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0))
print(sol.findPaths(m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1))
print(sol.findPaths(m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1))
