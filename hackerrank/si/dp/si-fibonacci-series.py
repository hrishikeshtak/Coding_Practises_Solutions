#!/usr/bin/python3

M = int(1e9 + 7)


# def fibonacci_series(N):
#     fibo = [0] * (N+1)
#     fibo[0] = 1
#     fibo[1] = 1
#     for i in range(2, N+1):
#         if fibo[i] == 0:
#             fibo[i] = fibo[i-1] + fibo[i-2]

#     return fibo[N] % M


def fibonacci_series(N):
    if N == 0 or N == 1:
        return 1
    a = 1
    b = 1
    c = 0
    for i in range(2, N+1):
        c = a + b
        a = b
        b = c

    return c % M

if __name__ == '__main__':
    for _ in range(int(input())):
        X = int(input())
        print(fibonacci_series(X))
