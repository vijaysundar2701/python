z= int(input())
if z > 1:
    for i in range(2,z):
        if (z% i) == 0:
            print("yes")
            break
    else:
        print("no")
else:
    print("no")
