import math


def factorial(n):

    return 1 if (n == 1 or n == 0) else n * factorial(n - 1);

class math:

    x = math.pi / 4
    n = 0
    print()
    try:
        n = int(input("enter n:"))
        a = x
        s = a
        i = 2

        while i <= n:
            a = (math.cos((math.pi/i)+(i*math.pi/2))/factorial(i))*math.pow((x-math.pi/4), i)
            s = s + a
            i += 1
        y1 = s
        y2 = (math.cos(x))
        print(y1, y2)
    except ValueError:
        print("incorrect value!")

