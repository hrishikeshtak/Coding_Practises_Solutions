#!/usr/bin/python3

max_people = 0
people_inside_tram = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    people_inside_tram -= a
    people_inside_tram += b
    if people_inside_tram > max_people:
        max_people = people_inside_tram

print(max_people)
