hi = int(input())
ab = list(map(int,input().split()))
st,lis = 0,[]
bc = [x for x in range(1,hi+1)]
for i in ab:
  if i in bc:
    bc.remove(i)
k = 0
for i in range(0,hi-1):
  p = ab[i]
  for j in range(i+1,hi):
    if p == ab[j]:
      if p < bc[k]:
        ab[j] = bc[k]
        st += 1
      else:
        ab[i] = bc[k]
        st += 1
      k += 1
print(st)
print(*ab)
