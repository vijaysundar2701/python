z=list(map(str,input()))
x=w=0
for i in range(0,len(z)-1):
    y=z[i]
    if int(y)!=0:
        for j in range(i+1,i+2):
            y=y+z[j]
            if int(y)<27 and int(y)>0: x=x+1
            elif int(y)==0: x=x-1
            else: break
if x!=1: w=x%2
print(x+w+1)
