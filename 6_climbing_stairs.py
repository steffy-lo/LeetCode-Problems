def bottom_up(n):
    # initialization
    solution_table = [0 for i in range(n)]

    # base case
    # n = 1
    solution_table[0] = 1
    if n > 1:
        # n = 2
        solution_table[1] = 2

        # n >= 3
        for i in range(2, n):
            solution_table[i] = solution_table[i-1] + solution_table[i-2]

    return solution_table[n-1]


def top_down(n):
    if n == 1 or n == 0:
        return 1
    else:
        return top_down(n-1) + top_down(n-2)


if __name__ == "__main__":
    print(bottom_up(3))
    print(top_down(3))
