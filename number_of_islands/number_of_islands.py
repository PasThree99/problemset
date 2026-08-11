class Solution:
    def visitIsland(self, grid, visited, i, j):
        queue = []
        queue.append([i, j])
        while len(queue) != 0:
            i, j = queue.pop()
        
            # Chech up
            x = i - 1
            y = j
            if x >= 0 and grid[x][y] == "1" and not visited[x][y]:
                visited[x][y] = True
                queue.append([x,y])
            
            # Chech down
            x = i + 1
            y = j
            if x < len(grid) and grid[x][y] == "1" and not visited[x][y]:
                visited[x][y] = True
                queue.append([x,y])

            # Chech left
            x = i
            y = j - 1
            if y >= 0 and grid[x][y] == "1" and not visited[x][y]:
                visited[x][y] = True
                queue.append([x,y])
            
            # Chech down
            x = i 
            y = j + 1
            if (y < len(grid[0]) and grid[x][y] == "1" and not visited[x][y]):
                visited[x][y] = True
                queue.append([x,y])
        return visited



    def numIslands(self, grid: list[list[str]]) -> int:
        visited = [ [False for j in range(len(grid[0]))] for i in range(len(grid))]
        islands = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not visited[i][j]:
                    visited[i][j] = True
                    visited = self.visitIsland(grid, visited, i, j)
                    islands += 1
        return islands
    

s = Solution()
print(s.numIslands([
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]))
print(s.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]]))