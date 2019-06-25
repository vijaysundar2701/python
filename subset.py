w,m=map(int,input().split())
v={int(v) for v in input().split()}
k={int(k) for k in input().split()} 
if(k.issubset(v)):
    print("YES")
else:
    print("NO")
