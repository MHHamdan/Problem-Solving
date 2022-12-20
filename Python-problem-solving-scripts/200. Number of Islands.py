class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # idea is to make connected components count 1 only by making them 0 once visited
        self.sum = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                self.sum += self.find_islands(grid, row, col)
        return self.sum
        
    def find_islands(self, grid,i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":
            grid[i][j] = "0"
            # go top left right bottom 
            # make all 1's 0 till all connected becomes zero
            # then return 1 as all connected componets forms one island
            # done
            self.find_islands(grid, i + 1, j)
            self.find_islands(grid, i, j-1)
            self.find_islands(grid, i-1, j)
            self.find_islands(grid, i, j + 1)
            return 1
        return 0
