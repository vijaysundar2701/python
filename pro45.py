vj=input()
if vj==vj[::-1]:
    print("yes")
else:
    val=vj.strip("0")
    if val==val[::-1]:
        print("yes")
    else:
        val=vj.lstrip("0")
        if val==val[::-1]:
            print("yes")
        else:
            print("no")
