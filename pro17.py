no,hi=input().split()
no=int(no)
hi=int(hi)
count=0
l=list(map(int,input().split()))
for i in range(no):
    for j in range(i+1,no):
        ss=0
        ss=l[i]+l[j]
        if(ss==hi):
            count+=1
            break
if(count==1):
    print("yes")
else:
    print("no")
