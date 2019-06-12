y=int(input())
r=0
temp=y
while(y>=1):
    a=int(y%10)
    r=int(r+a*a*a)
    y=int(y/10)
if temp==r:
    print("yes")
else:
    print("no")
    
