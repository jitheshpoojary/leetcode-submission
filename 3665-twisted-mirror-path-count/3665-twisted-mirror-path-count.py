class Solution(object):
    def uniquePaths(self, grid):
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        memo = {}

        def reflect(r, c, d):
            if r < 0 or r >= m or c < 0 or c >= n:
                return None

            if grid[r][c] == 0:
                return (r, c)

            key = (r, c, d)
            if key in memo:
                return memo[key]

            if d == 0:
                ans = reflect(r + 1, c, 1)
            else:
                ans = reflect(r, c + 1, 0)

            memo[key] = ans
            return ans

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                cur = dp[i][j]
                if not cur:
                    continue

                if j + 1 < n:
                    if grid[i][j + 1] == 0:
                        dp[i][j + 1] = (dp[i][j + 1] + cur) % MOD
                    else:
                        nxt = reflect(i, j + 1, 0)
                        if nxt:
                            r, c = nxt
                            dp[r][c] = (dp[r][c] + cur) % MOD

                if i + 1 < m:
                    if grid[i + 1][j] == 0:
                        dp[i + 1][j] = (dp[i + 1][j] + cur) % MOD
                    else:
                        nxt = reflect(i + 1, j, 1)
                        if nxt:
                            r, c = nxt
                            dp[r][c] = (dp[r][c] + cur) % MOD

        return dp[m - 1][n - 1]