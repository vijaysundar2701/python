import math
import functools
aa,zz=map(int,input().split())
List=[int(i) for i in input().split()]
for i in range(zz):
    mn,p=map(int,input().split())
    vj=functools.reduce(math.gcd,List[mn-1:p])
    print(vj)
