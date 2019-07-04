z, y, x, w = map(int, input().split())
c = 0
a =y-x
if (a >= 0):
    d = (z-x)*2
    for i in range (w):
        if (i == w-1):
             d =d/ 2
        if (a < d):
            a = y
            c += 1
        a = a - d
        if (a < 0):
            count = -1
            break
        d = 2*z - d

    print (c)
else:
    print (-1)
