class Solution:

  def countIslands(self, grid: list[list[int]], k: int) -> int:
    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]
    count = 0

    def dfs(r, c):
      # Mark current cell visited and return its value plus neighbors
      visited[r][c] = True
      total = grid[r][c]
      for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < m and 0 <= nc < n:
          if grid[nr][nc] != 0 and not visited[nr][nc]:
            total += dfs(nr, nc)
      return total

    for i in range(m):
      for j in range(n):
        if grid[i][j] != 0 and not visited[i][j]:
          island_sum = dfs(i, j)
          if island_sum % k == 0:
            count += 1

    return count
