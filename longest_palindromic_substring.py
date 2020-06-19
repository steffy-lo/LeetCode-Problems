def main(string):
    # A table of booleans, storing the results of whether the substring at index i to j is a palindrome
    # initialize all to False
    palindrome_table = [[False for i in range(len(string))] for j in range(len(string))]

    # 2 base cases:
    # (1) all substrings of length 1 are palindromes
    for k in range(len(string)):
        palindrome_table[k][k] = True

    # (2) all substring of length 2 are palindromes if they are the same letters
    start = 0
    length = 1
    for k in range(len(string) - 1):
        if string[k] == string[k+1]:
            start = k
            length = 2
            palindrome_table[k][k+1] = True

    # For substring of lengths k, where k > 2
    for k in range(2, len(string)):
        for i in range(len(string) - k):
            j = i + k
            if palindrome_table[i + 1][j - 1] and string[i] == string[j]:
                palindrome_table[i][j] = True
                if k + 1 > length:
                    start = i
                    length = k + 1

    return string[start: start + length]


if __name__ == "__main__":
    print(main("racecar"))

