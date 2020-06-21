def main(m, n):
    # initialization
    solution_table = [[0 for i in range(m)] for j in range(n)]

    # base case
    # case 1: n = 1, only one way to traverse
    for j in range(m):
        solution_table[0][j] = 1

    # case 2: m = 1, only one way to traverse
    for i in range(n):
        solution_table[i][0] = 1

    for i in range(1, n):
        for j in range(1, m):
            solution_table[i][j] = solution_table[i-1][j] + solution_table[i][j-1]

    return solution_table[n-1][m-1]


if __name__ == "__main__":
    print(main(7, 3))

