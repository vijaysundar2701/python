f=int(input())
q=0
temp=f
while(f!=0):
    p=int(f%10)
    q=int(q*10+p)
    f=int(f/10)
if(temp==q):
    print("yes")
else:
    print("no")
