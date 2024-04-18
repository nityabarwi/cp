def islandPerimeter(grid):
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter

# Test Cases
grid1 = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
grid2 = [[1]]
grid3 = [[1,0]]

print(islandPerimeter(grid1))
print(islandPerimeter(grid2))
print(islandPerimeter(grid3))