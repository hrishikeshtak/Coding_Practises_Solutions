#!/usr/bin/python3

"""
Ada the Ladybug has many friends. They always celebrate
something and Ada has to buy them gifts. It is pretty costly
so she have decided to unfriend some of them. What is the
maximum of money she can spare?
"""
from collections import defaultdict


def ada_and_friends(friends_dict, K):
    # print(friends_dict)
    friends_dict = sorted(friends_dict.items(),
                          key=lambda t: t[1],
                          reverse=True)
    # print(friends_dict)
    ans = 0
    try:
        for i in range(K):
            ans += friends_dict[i][1]
    except Exception:
        pass

    return ans


if __name__ == '__main__':
    friends_dict = defaultdict(lambda: 0)
    Q, K = map(int, input().split())
    for _ in range(Q):
        name, expenses = input().split()
        friends_dict[name] += int(expenses)
    print(ada_and_friends(friends_dict, K))
