class Solution:

    def isValidElem(self, i,j):
        if (i >= 0 and j >= 0 and 
           i < self.grid_dimensions[0] and j < self.grid_dimensions[1]):
            return True
        else:
            return False 

    def orangesRotting(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if n == 0:
            print("Empty matrix")
            return -1
        
        m = len(grid[0])
        if m == 0:
            print("Empty rows")
            return -1
        
        self.grid_dimensions = [n,m]

        self.time_matrix = [[-1 for j in range(m)] for i in range(n)]
        
        foundRottenOrange = False
        freshOrangesCount = 0
        rottenOrangesQueue = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    foundRottenOrange = True
                    self.time_matrix[i][j] = 0
                    rottenOrangesQueue.append([i, j])
                elif grid[i][j] == 1:
                    self.time_matrix[i][j] = 9999
                    freshOrangesCount += 1
        
        if not freshOrangesCount:
            return 0
        
        if not foundRottenOrange:
            return -1
        
        mins = 0
        while len(rottenOrangesQueue) != 0:
            newQueue = []
            for orange in rottenOrangesQueue:
                actualTime = self.time_matrix[orange[0]][orange[1]]

                print(orange)
                
                # Check the apple above
                i = orange[0] - 1
                j = orange[1]
                if (i >= 0) and grid[i][j] == 1:
                    self.time_matrix[i][j] = min(self.time_matrix[i][j], actualTime + 1)
                    grid[i][j] = 2
                    freshOrangesCount -= 1
                    newQueue.append([i, j])
                
                # Check the apple below
                i = orange[0] + 1
                j = orange[1]
                if (i < n) and grid[i][j] == 1:
                    self.time_matrix[i][j] = min(self.time_matrix[i][j], actualTime + 1)
                    grid[i][j] = 2
                    freshOrangesCount -= 1
                    newQueue.append([i, j])
                
                # Check the apple on the left
                i = orange[0]
                j = orange[1] - 1
                if (j >= 0) and grid[i][j] == 1:
                    self.time_matrix[i][j] = min(self.time_matrix[i][j], actualTime + 1)
                    grid[i][j] = 2
                    freshOrangesCount -= 1
                    newQueue.append([i, j])
                
                # Check the apple on the rigth
                i = orange[0]
                j = orange[1] + 1
                if (j < m) and grid[i][j] == 1:
                    self.time_matrix[i][j] = min(self.time_matrix[i][j], actualTime + 1)
                    grid[i][j] = 2
                    freshOrangesCount -= 1
                    newQueue.append([i, j])

            rottenOrangesQueue = newQueue.copy()
            newQueue.clear()

            mins += 1

        return mins - 1 if freshOrangesCount == 0 else -1

            
s = Solution()

print(s.orangesRotting([[0]]))
