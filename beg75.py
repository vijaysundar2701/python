v=input()
r=int(len(v)/2)
d=len(v)%2
s=list(v)
if d==0:
    for i in range(r-1,r+1):
        s[i]="*"
else:
    s[r]="*"
print(*s,sep="")
