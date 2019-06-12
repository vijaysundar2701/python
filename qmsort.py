q=int(input())
r=list(map(int,input().split()))
r.sort()
for i in range(0,len(r)):
  print(r[i],end=' ')
