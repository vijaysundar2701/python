hh,ee=map(int,input().split())
tt=[]
xy=0
for i in range(hh):
    tt.append(list(map(int,input().split())))   
for i in range(hh):
    for j in range(ee-1):
        for k in range(j+1,ee+1):
            if tt[i][j:k]==[1]*len(tt[i][j:k]):
                 if all(tt[p+i][j:k]==[1]*len(tt[p+i][j:k]) for p in range(len(tt[i][j:k])-1)):
                     if len(tt[i][j:k])>xy:
                        xy=len(tt[i][j:k])
if len(tt)==1 and len(tt[0])==1 and tt[0][0]==1:
    print(1)
for i in range(xy):
    print(*[1]*xy)
