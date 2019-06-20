n=int(input())
li=[]
h=(input().split())[:n]
for j in range(0,n):
    for k in range(j+1,n):
        if h[j]==h[k]:
            li.append(h[k])
            break
if(len(li)==0):
    print("unique")
else:
    li.sort()
    r=set(li)
    for y in r:
        print(*y,end=' ')
        
