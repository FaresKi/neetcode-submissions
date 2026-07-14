class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                cell = grid[row][col]
                if cell == "1":
                    count += 1
                    grid[row][col] = "0"
                    queue = deque([(row, col)])
                    while queue:
                        r, c = queue.popleft()

                        for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                            nr, nc = r + dr, c + dc

                            if (
                                len(grid) > nr >= 0
                                and len(grid[row]) > nc >= 0
                                and grid[nr][nc] == "1"
                            ):
                                # we won't increase the count because they are neighbors
                                # to the current cell
                                grid[nr][nc] = "0"
                                queue.append((nr, nc))

        return count
