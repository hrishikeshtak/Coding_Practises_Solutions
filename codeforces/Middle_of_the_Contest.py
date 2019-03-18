#!/usr/bin/python3


def contest(h1, m1, h2, m2):
    # first calculate total difference minutes
    diff_hrs = h2 - h1
    diff_mins = m2 - m1
    # convert to mins
    total_mins = (diff_hrs * 60) + diff_mins
    half_mins = total_mins // 2

    # print(diff_hrs, diff_mins)
    # print(total_mins)
    # convert mins to hrs:mins
    h3 = h1 + (half_mins // 60)
    m3 = m1 + (half_mins % 60)

    if m3 >= 60:
        m3 = m3 % 60
        h3 = h3 + 1
    if h3 < 10:
        h3 = "0" + str(h3)
    if m3 < 10:
        m3 = "0" + str(m3)
    print("{}:{}".format(h3, m3))


if __name__ == "__main__":
    h1, m1 = map(int, input().split(":"))
    h2, m2 = map(int, input().split(":"))
    contest(h1, m1, h2, m2)
