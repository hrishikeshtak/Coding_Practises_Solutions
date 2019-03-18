#!/usr/bin/python3

# count the number of trailing 0s in factorial of a given number.
for _ in range(int(input())):
    n = int(input())
    # no of 0's == no of 5's till that number
    # count = n // 5  # no of 5, repeating only 1 times
    # count += n // 25   # no of 5, repeating 2 times
    # count += n // 125  # no of 5, repeating 3 times
    temp = 5
    count = 0
    if n <= (temp - 1):
        print(count)
    else:
        while temp <= n:
            count += n // temp
            # divide by multiple of 5 and take sum
            temp = temp * 5
        print(count)

