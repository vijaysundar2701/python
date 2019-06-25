w=int(input())
u=list(map(int,input().split()))
for x in range(0,w-2):
    for y in range(x+1,w-1):
        for z in range(y+1,w):
            if(u[x]+u[y]==u[z]):
                print(u[x], u[y], u[z])
