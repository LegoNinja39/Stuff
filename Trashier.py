s = "   "
ss = ""


def x(y): return print("Yes") if not y or y.isspace() else print("No")


x(s)
x(ss)


def tHrInc(dataLen: int) -> None:
    for hr in range(dataLen):
        if hr > 42:
            activeHr = (hr - 42) * 3 + 42
        else:
            activeHr = hr
        print(activeHr)


tHrInc(70-1-1)
