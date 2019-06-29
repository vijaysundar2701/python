vh=int(input())
vj=list(map(int,input().split()))
nm=si=[]
for i in range(0,vh):
    nm=list(bin(vj[i]))
    nm=nm[2:]
    si.append(nm)
si=sorted(si)
si=si[::-1]
for i in range(0,vh):
    yy=1
    zz=0
    for j in range(len(si[i])-1,-1,-1):
        zz=zz+(int(si[i][j])*yy)
        yy=yy*2
    print(zz)
