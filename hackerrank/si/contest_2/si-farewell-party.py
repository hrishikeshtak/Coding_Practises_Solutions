#!/usr/bin/python3


def farewell_party(arrival, departure):
    # print("arrival: ", arrival)
    # print("departure: ", departure)
    arrival.sort()
    departure.sort()
    # print("arrival: ", arrival)
    # print("departure: ", departure)

    N = len(arrival)
    M = len(departure)

    cnt = 0
    max_cap = -(1 << 31)
    i = 0
    j = 0
    while i < N and j < M:
        if arrival[i] <= departure[j]:
            cnt += 1
            max_cap = max(max_cap, cnt)
            # print(cnt, max_cap)
            i += 1
        else:
            cnt -= 1
            j += 1
    return max_cap


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        arrival = []
        departure = []
        for _ in range(N):
            x, y = map(int, input().split())
            arrival.append(x)
            departure.append(y)

        print(farewell_party(arrival, departure))
