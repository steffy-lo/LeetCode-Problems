def main1(num_array):

    max_sum = float("-inf")
    start = 0
    end = 1

    for i in range(1, len(num_array)):
        sum = 0
        for j in range(i, len(num_array)):
            sum += num_array[j]
            if sum > max_sum:
                max_sum = sum
                start = i
                end = j + 1

    print("The array " + str(num_array[start:end]) + " has the largest sum of " + str(max_sum))


def main2(num_array):
    # initialize the array where we store our computed solutions
    max_sums = [float("-inf") for i in range(len(num_array))]

    # base case
    max_sums[0] = max(float("-inf"), num_array[0])

    for j in range(1, len(num_array)):
        max_sums[j] = max(max_sums[j-1] + num_array[j], num_array[j])

    print("The maximum subarray is " + str(max(max_sums)))


if __name__ == "__main__":
    main1([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    main2([-2, 1, -3, 4, -1, 2, 1, -5, 4])

