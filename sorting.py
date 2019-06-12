u=int(input())
v=list(map(int,input().split()))[:u]
print(*sorted(v),end=' ')
