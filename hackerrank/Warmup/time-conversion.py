#!/bin/python3


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hh, mm, ss = s.split(':')
    ss = ss[:-2]
    if s[-2:].lower() == 'am':
        if hh == '12':
            return "{}:{}:{}".format('00', mm, ss)
        else:
            return "{}:{}:{}".format(hh, mm, ss)
    else:
        if hh == '12':
            return "{}:{}:{}".format(hh, mm, ss)
        return "{}:{}:{}".format(12 + int(hh), mm, ss)


if __name__ == '__main__':
    # s = input()
    s = "07:05:45PM"
    result = timeConversion(s)
    print(result)
