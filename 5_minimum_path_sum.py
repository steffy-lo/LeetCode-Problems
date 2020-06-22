def main(grid):
    # We can assume n >= 1, m >= 1
    n = len(grid)
    m = len(grid[0])
    solution_table = [[0 for i in range(m)] for j in range(n)]

    # base cases
    # n = 1
    for i in range(m):
        if i == 0:
            solution_table[0][i] = grid[0][i]
        else:
            solution_table[0][i] = solution_table[0][i-1] + grid[0][i]

    # m = 1
    for j in range(n):
        if j == 0:
            solution_table[j][0] = grid[j][0]
        else:
            solution_table[j][0] = solution_table[j-1][0] + grid[j][0]

    for i in range(1, n):
        for j in range(1, m):
            solution_table[i][j] = min(solution_table[i][j-1] + grid[i][j], solution_table[i-1][j] + grid[i][j])

    return solution_table[n-1][m-1]


if __name__ == "__main__":
    print(main([
      [1, 3, 1],
      [1, 5, 1],
      [4, 2, 1]
    ]))

