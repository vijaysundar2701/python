az,by=input().split()
az=int(az)
by=int(by)
d=''
u=2
if(az+by<=3):
    for i in range(0,az+by):
        if(i%2!=0):
            d=d+'0'
        else:
            d=d+'1'
else:    
    for i in range(0,az+by):
        if(i==u):
            d=d+'0'
            if(u==by):
                u=u+2
            else:
                u=u+3
        else:
            d=d+'1'
x=len(d)-1
if(int(d[x])==0):
    print('-1')
elif az==1 and by==2: print("011")
else:
    print(d)
