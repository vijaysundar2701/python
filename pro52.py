vj,vk=list(map(int,input().split()))
zin,ain=list(map(int,input().split()))
yin,bin=list(map(int,input().split()))
xin,cin=list(map(int,input().split()))
mn=ain-vk
kl=bin-cin
qr=yin-zin
st=xin-vj
if (kl==mn==qr==st):
    print("yes")
else:
    print("no")
