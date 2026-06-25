class Solution:
    def inBounds(self, grid, i, j):
        length = len(grid)
        width = len(grid[0])
        return i < length and i >=0 and j < width and j >= 0

    def checkSurround(self, grid, vis, i, j):
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        for dir in dirs:
            dx, dy = dir
            nx, ny = i + dx, j + dy
            if self.inBounds(grid, nx, ny) and vis[nx][ny] == 0:
                if grid[nx][ny] == "1":
                    vis[nx][ny] = 1
                    self.checkSurround(grid, vis, nx, ny)
                vis[nx][ny] = 1

    def debugPrint(self, mat):
        for i in range(len(mat)):
            print(mat[i])

    def numIslands(self, grid: List[List[str]]) -> int:
        vis = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if vis[i][j] == 1:
                    continue
                else:
                    if grid[i][j] == "1":
                        #check surrounding
                        vis[i][j] = 1
                        self.debugPrint(vis)
                        self.checkSurround(grid, vis, i, j)
                        print("1")
                        self.debugPrint(grid)
                        print()
                        self.debugPrint(vis)
                        cnt += 1
                    elif grid[i][j] == "0":
                        # mark as vis
                        vis[i][j] = 1
        return cnt
        

