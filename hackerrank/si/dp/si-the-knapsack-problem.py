#!/usr/bin/python3

# 1 based index


def knapsack_problem(weight, value, K, N):
    # print("weight ", weight)
    # print("value ", value)
    dp = [[0 for i in range(K+1)] for j in range(N+1)]

    # import pdb; pdb.set_trace()
    for i in range(1, N+1):
        for j in range(0, K+1):
            if j >= weight[i]:
                dp[i][j] = max(dp[i-1][j-weight[i]] + value[i], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    # print(dp)
    return dp[N][K]


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
