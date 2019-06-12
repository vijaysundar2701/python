mini,maxi=map(int,input().split())
li=[]
for i in range(mini+1,maxi):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            li.append(i)
print(*li,end='  ')
            
