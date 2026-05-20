from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0


        griddy = grid

        for i in range(len(griddy)):
            for j in range(len(griddy[i])):
                if griddy[i][j] == "1":
                    count +=1
                    loc = (i,j)
                    self.dfs(loc,griddy)


        return count

    def dfs(self,loc,grid):

        queue = deque([loc])

        while queue:

            size = len(queue)

            for i in range(size):

                r,c = queue.popleft()

                grid[r][c] = "0"

                #four directions:
                #up: -1, 0
                if(r-1 >=0 and r -1 < len(grid)):
                    if(grid[r-1][c] == "1"):
                        queue.append((r-1,c))

                #down: 1,0
                if(r+1 >=0 and r + 1 < len(grid)):
                    if(grid[r+1][c] == "1"):
                        queue.append((r+1,c))

                #left: 0, -1
                if(c-1 >=0 and c-1 < len(grid[r])):
                    if(grid[r][c-1] == "1"):
                        queue.append((r,c-1))

                #right: 0, 1
                if(c+1 >=0 and c+1 < len(grid[r])):
                    if(grid[r][c+1] == "1"):
                        queue.append((r,c+1))


        





    

        