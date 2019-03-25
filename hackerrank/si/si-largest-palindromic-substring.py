#!/usr/bin/python3

# optimize = O(N2)


def length_of_largest_palindrome(string, N):
    max_length = 1
    p1 = p2 = 0
    start = 0

    for i in range(1, N):
        # Find even length palindrome string
        p1 = i - 1
        p2 = i
        while p1 >= 0 and p2 < N and string[p1] == string[p2]:
            max_length = max(max_length, p2 - p1 + 1)
            start = p1
            p1 = p1 - 1
            p2 = p2 + 1

        # Find odd length palindrome string
        p1 = i - 1
        p2 = i + 1
        while p1 >= 0 and p2 < N and string[p1] == string[p2]:
            max_length = max(max_length, p2 - p1 + 1)
            start = p1
            p1 = p1 - 1
            p2 = p2 + 1

    # print("Longest palindrome substring is: %s" % (
    #     string[start: start+max_length]))

    return max_length


if __name__ == '__main__':
    for _ in range(int(input())):
        N = int(input())
        string = input()
        print(length_of_largest_palindrome(string, N))
