vj=int(input())
z=2
n=3
vk=3
while z<vj+1:
    if n==1:
        n=2*vk
        vk=n
    else:
        n=n-1
    z=z+1
print(n)
