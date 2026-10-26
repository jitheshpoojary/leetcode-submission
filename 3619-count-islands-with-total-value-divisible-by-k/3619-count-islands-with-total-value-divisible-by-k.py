from collections import deque

class Solution:
    def countIslands(self, grid, k):
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not visited[i][j]:
                    q = deque([(i, j)])
                    visited[i][j] = True

                    total = 0

                    while q:
                        r, c = q.popleft()
                        total += grid[r][c]

                        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            nr, nc = r + dr, c + dc

                            if (
                                0 <= nr < m
                                and 0 <= nc < n
                                and grid[nr][nc] > 0
                                and not visited[nr][nc]
                            ):
                                visited[nr][nc] = True
                                q.append((nr, nc))

                    if total % k == 0:
                        ans += 1

        return ans