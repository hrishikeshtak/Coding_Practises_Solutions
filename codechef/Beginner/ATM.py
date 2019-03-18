x, y = map(float, input().split())
if y >= (x + 0.50) and x % 5 == 0:
    print("{:.2f}".format(y - (x + 0.5)))
else:
    print("{:.2f}".format(y))
