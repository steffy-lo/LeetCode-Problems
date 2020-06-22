def main(obs_grid):
    # initialization
    # assume n >= 1, m >= 1
    n = len(obs_grid)
    m = len(obs_grid[0])
    solution_table = [[0 for i in range(m)] for j in range(n)]

    # base case
    # case 1: n = 1, only one way to traverse or zero thereafter if there is an obstacle
    blocked = False
    for j in range(m):
        if obs_grid[0][j] == 1 or blocked:
            solution_table[0][j] = 0
            blocked = True
        else:
            solution_table[0][j] = 1

    # case 1: m = 1, only one way to traverse or zero thereafter if there is an obstacle
    blocked = False
    for i in range(n):
        if obs_grid[i][0] == 1 or blocked:
            solution_table[i][0] = 0
            blocked = True
        else:
            solution_table[i][0] = 1

    for i in range(1, n):
        for j in range(1, m):
            if obs_grid[i][j] == 1:
                solution_table[i][j] = 0
            else:
                solution_table[i][j] = solution_table[i-1][j] + solution_table[i][j-1]

    return solution_table[n-1][m-1]


if __name__ == "__main__":
    print(main([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]))
