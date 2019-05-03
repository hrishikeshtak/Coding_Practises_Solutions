#!/usr/bin/python3

# 1 based index


def knapsack_problem(weight, value, K, N):
    if K == 0 or N == 0:
        return 0

    if weight[N] > K:
        return knapsack_problem(weight, value, K, N-1)
    else:
        return max(knapsack_problem(weight, value, K-weight[N], N-1) + value[N],
                   knapsack_problem(weight, value, K, N-1))


if __name__ == '__main__':
    for _ in range(int(input())):
        K, N = map(int, input().split())
        weight = [0]
        value = [0]
        for _ in range(0, N):
            i, j = map(int, input().split())
            weight.append(i)
            value.append(j)
        print(knapsack_problem(weight, value, K, N))
