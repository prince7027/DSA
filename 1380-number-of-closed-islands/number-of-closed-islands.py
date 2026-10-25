class Solution:
  def closedIsland(self, grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])

    def dfs(i, j):
      if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 0:
        return
      grid[i][j] = 1  # Mark as visited/water
      dfs(i + 1, j)
      dfs(i - 1, j)
      dfs(i, j - 1)
      dfs(i, j + 1)

    # 1. Eliminate land connected to the borders
    for i in range(m):
      for j in range(n):
        if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and grid[i][j] == 0:
          dfs(i, j)

    # 2. Count remaining closed islands
    ans = 0
    for i in range(m):
      for j in range(n):
        if grid[i][j] == 0:
          dfs(i, j)
          ans += 1

    return ans
