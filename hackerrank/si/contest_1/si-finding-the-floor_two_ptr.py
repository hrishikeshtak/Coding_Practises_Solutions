#!/usr/bin/python3

# two pointer


def quick_sort(arr, lo, hi):
    if lo < hi:
        p = partition(arr, lo, hi)
        quick_sort(arr, lo, p)
        quick_sort(arr, p+1, hi)


def partition(arr, lo, hi):
    i = lo - 1
    pivot = arr[hi-1]
    for j in range(lo, hi):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[hi-1] = arr[hi-1], arr[i+1]
    return i + 1


def binary_search(arr, X):
    lo = 0
    hi = len(arr) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] == X:
            return mid
        elif arr[mid] < X:
            lo = mid + 1
        else:
            hi = mid - 1


def finding_the_floor(arr, Q, query):
    ans = -(1 << 31)
    ans_q = []
    p1 = 0  # arr
    p2 = 0  # Q
    while p1 < len(arr) and p2 < len(Q):
        if Q[p2] < arr[p1]:
            ans = arr[p1]
            p1 += 1
        elif arr[p1] == Q[p2]:
            ans = arr[p1]
            ans_q.append(ans)
            p1 += 1
            p2 += 1
        else:
            ans_q.append(ans)
            p2 += 1
    print("ans_q: ", ans_q)
    print("query: ", query)
    for q in query:
        index = binary_search(Q, q)
        print("q: %s, index: %s" % (q, index))
        print(ans_q[index])


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    # print(arr)
    quick_sort(arr, 0, len(arr))
    # print(arr)
    Q = []
    for _ in range(int(input())):
        X = int(input())
        Q.append(X)
    # take backup of Q
    query = Q[:]
    # print("Q: ", Q)
    quick_sort(Q, 0, len(Q))
    # print("Q: ", Q)
    finding_the_floor(arr, Q, query)
