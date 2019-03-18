#!/usr/bin/python3

pos = input()
count = 1
if len(pos) < 7:
    print("NO")
else:
    for i in range(len(pos)-1):
        if pos[i] == pos[i+1]:
            count += 1
        else:
            count = 1

        if count == 7:
            print("YES")
            break
    if count != 7:
        print("NO")
