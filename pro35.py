vj=input()
lis=list(set(vj))
xy=1
h=0
check=False
while True:
    ch=lis[h]
    for j in range(0,len(vj)-xy):
        if ch in vj[j:j+xy]:
            check=True
        else:
            check=False
            h+=1
            if h>=len(lis):
             h=0
             xy+=1
            break

    if check==True:
        break
print(xy)
