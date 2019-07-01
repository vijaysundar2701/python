vi=int(input())
Bb=list(map(int,input().split()))
Cc=[]
se=1
for i in Bb:
  if i not in Cc:
    Cc.append(i)
for i in range(len(Cc)-1):
  if (Cc[i]<Cc[i+1]):
    se+=1
print(se)
