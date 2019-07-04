vj = int(input())
h = []
di = vj//2 + vj
for i in range(1,vj+1):
  if i%2==0:
    h.append(i)
for i in range(1,vj+1):
  if i%2!=0:
    h.append(i)
for i in range(1,vj+1):
  if i%2==0:
    h.append(i)
print(di)
print(*h)
