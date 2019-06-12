z= int(input())
if z > 1:
    for i in range(2,z):
        if (z% i) == 0:
            print("no")
            break
    else:
        print("yes")
else:
    print("no")
