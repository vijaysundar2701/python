hi,o = map(int,input().split())
z = list(map(int,input().split()))
b,cin = 0,[]
for i in range(0,len(z)):
  t = i
  for p in range(0,len(z)):
    for l in range(0,o):
      if l == o-1:
        try:
          b += z[p+i]
        except IndexError:
            t = t-1
            b +=z[t]
      else:
        b += z[i]
    cin.append(b)
    b = 0
for i in range(0,len(z),o):
  b = sum(z[i:i+o])
  cin.append(b)
print(*sorted(set(cin)))
