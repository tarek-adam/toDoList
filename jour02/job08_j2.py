def get_Numbers():
    l = [1, 2, 3, 4, 5]

    x = l[2] + l[4]
    l[3] = x
    return l
print(get_Numbers())

One_Number = get_Numbers()
print(One_Number[-1])


