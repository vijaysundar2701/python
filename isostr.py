a,b=map(str,input().split())
if(len(a) != len(b)):
    print('no')
x=[a.count(char1) for char1 in a]
y=[b.count(char1) for char1 in b]
if(x==y):
    print('yes')
else:
    print('no')
