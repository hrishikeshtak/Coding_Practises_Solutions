#!/usr/bin/python3

actualDay, actualMonth, actualYear = \
    map(int, (input().split()))
expectedDay, expectedMonth, expectedYear = \
    map(int, (input().split()))

if (actualDay, actualMonth, actualYear) == (
        expectedDay, expectedMonth, expectedYear):
        print(0)

elif (actualYear, actualMonth) == (expectedYear, expectedMonth):
    print(15 * (actualDay - expectedDay))

elif (actualYear) == (expectedYear):
    if actualMonth <= expectedMonth and \
       actualDay <= expectedDay:
        print(0)
    else:
        print(500 * (actualMonth - expectedMonth))

elif actualYear > expectedYear:
    print(10000)
else:
    print(0)
