small,big=map(int,input().split())
lis=[]
for i in range(small+1,big):
    if i%2!=0:
        lis.append(i)
print(*lis,end='  ')
