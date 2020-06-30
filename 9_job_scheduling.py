class Job:
    def __init__(self, start, finish, profit):
        self.start = start
        self.finish = finish
        self.profit = profit


"""
Function to find the index of the last job that doesn't conflict with the given job (unoptimized)
"""
def get_last_non_conflicting_job_unopt(jobs, n):
    for i in reversed(range(n)):
        if jobs[i].finish <= jobs[n].start:
            return i
    return -1  # if no non-conflicting job is found


"""
Function to find the index of the last job that doesn't conflict with the given job (optimized with binary search)
"""
def get_last_non_conflicting_job(jobs, n):
    low = 0
    high = n
    while low <= high:
        mid = (low + high) // 2
        if jobs[mid].finish <= jobs[n].start:
            if jobs[mid + 1].finish <= jobs[n].start:
                low = mid + 1
            else:
                return mid
        else:
            high = mid - 1

    return -1  # if no non-conflicting job is found


def main(startTime, endTime, profit) -> int:
    jobs = []
    for i in range(len(profit)):
        jobs.append(Job(startTime[i], endTime[i], profit[i]))
    # sort jobs in increasing order of their finish times
    jobs.sort(key=lambda x: x.finish)

    # initialize max profit table
    maxProfit = [0 for i in range(len(jobs))]

    maxProfit[0] = jobs[0].profit

    for i in range(1, len(jobs)):
        # find the index of last non-conflicting job with current job
        j = get_last_non_conflicting_job(jobs, i)

        # include the current job with its non-conflicting job
        profit = jobs[i].profit
        if j != -1:
            profit += maxProfit[j]

        # store the maximum profit by including or excluding the current job
        maxProfit[i] = max(profit, maxProfit[i-1])

    return maxProfit[len(jobs) - 1]


if __name__ == "__main__":
    # print(main([Job(1, 3, 50), Job(2, 4, 10), Job(3, 5, 40), Job(3, 6, 70)]))
    # print(main([Job(1, 2, 20), Job(2, 5, 20), Job(3, 10, 100), Job(4, 6, 70), Job(6, 9, 60)]))
    # print(main([Job(1, 2, 5), Job(1, 3, 6), Job(1, 4, 4)]))
    print(main([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]))
