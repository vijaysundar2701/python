u=int(input())
v=list(map(int,input().split()))[:u]
v.sort()
print(v[int(len(v)/2)])
