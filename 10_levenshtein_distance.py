def top_down(word1, word2):
    if len(word1) == 0:
        return len(word2)
    if len(word2) == 0:
        return len(word1)

    cost = 0 if word1[-1] == word2[-1] else 1

    return min(top_down(word1[:-1], word2) + 1, top_down(word1, word2[:-1]) + 1, top_down(word1[:-1], word2[:-1]) + cost)


def bottom_up(word1, word2):
    dist_table = [[0 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]

    for i in range(1, len(word1) + 1):
        dist_table[i][0] = i  # base case

    for j in range(1, len(word2) + 1):
        dist_table[0][j] = j  # base case

    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            if word1[i-1] == word2[j-1]:
                dist_table[i][j] = dist_table[i-1][j-1]
            else:
                dist_table[i][j] = 1 + min(dist_table[i-1][j],
                                           dist_table[i][j-1],
                                           dist_table[i-1][j-1])

    return dist_table[len(word1)][len(word2)]


if __name__ == "__main__":
    print(top_down("kitten", "sitting"))  # time limit exceeded on LeetCode... Boo...
    print(bottom_up("intention", "execution"))  # ギリギリだね

