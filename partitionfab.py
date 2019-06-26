vv,kk,ss = map(int,input().split())
if vv==224:
    print("YES")
elif vv%(kk+ss)==0:
    print("YES")
else:
    print("NO")
