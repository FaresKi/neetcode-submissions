class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, columns = len(image), len(image[0])

        def get_neighbors(coordinates, color):
            row, column = coordinates
            delta_row = [-1,0,1,0]
            delta_col = [0,1,0,-1]
            for i in range(len(delta_row)):
                neighbor_row = row + delta_row[i]
                neighbor_col = column + delta_col[i]
                if 0 <= neighbor_row < rows and 0 <= neighbor_col < columns:
                    if image[neighbor_row][neighbor_col]==color:
                        yield neighbor_row, neighbor_col

        def bfs(root):
            queue = deque([root])
            visited = [[False for c in range(columns)] for r in range(rows)]
            row, column = root
            original_color = image[row][column]
            image[row][column] = color
            visited[row][column] = True
            while(len(queue)>0):
                node = queue.popleft()
                for neighbor in get_neighbors(node, original_color):
                    row, column = neighbor
                    if visited[row][column]:
                        continue
                    image[row][column]=color
                    queue.append(neighbor)
                    visited[row][column] = True

        bfs((sr, sc))
        return image
