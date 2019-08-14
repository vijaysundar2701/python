h=input()
c=0
k=0
for i in h:
    if(i.isalpha()):
        c=c+1
    elif(i.isdigit()):
        k=k+1
    else:
        d=0
if c!=0 and k!=0:
    print("Yes")
else:
    print("No")
