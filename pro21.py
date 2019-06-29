pq=int(input())
rs=list(map(int,input().split()))
avg=int(pq/2)
la=rs[:avg]
lb=rs[avg::]
if ((sum(la)//len(la))==(sum(lb)//len(lb))):
    print("yes")
else:
    print("no")
