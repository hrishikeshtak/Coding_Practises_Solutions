#!/usr/bin/env python3

# collections.Counter()

# A counter is a container that stores elements as dictionary keys,
# and their counts are stored as dictionary values.

# Task

# Raghu is a shoe shop owner. His shop has X number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are N number of customers who are willing to pay xi amount of
# money only if they get the shoe of their desired size.

# Your task is to compute how much money  earned.

# Input Format

# The first line contains X, the number of shoes.
# The second line contains the space separated list of all
# the shoe sizes in the shop.
# The third line contains N, the number of customers.
# The next N lines contain the space separated values of the shoe size
# desired by the customer and x, the price of the shoe.

# Output Format

# Print the amount of money earned by Raghu

from collections import Counter

shoes_count = int(input())
shoes_size_list = list(map(int, input().split()[:shoes_count]))

shoes_size_counter = Counter(shoes_size_list)

customer_count = int(input())

raghu_earning = 0

for i in range(customer_count):
    shoe_size, price = map(int, input().split())
    if shoe_size in shoes_size_counter:
        if shoes_size_counter[shoe_size] > 0:
            raghu_earning += int(price)
            shoes_size_counter[shoe_size] -= 1
        else:
            continue

print(raghu_earning)
